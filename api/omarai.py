"""Loopback-only HTTP API for Omarai; no external network calls."""
from __future__ import annotations
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
from pathlib import Path
from agents.omarai import LeadStore, analyze, normalize

DASHBOARD = Path(__file__).resolve().parents[1] / "web" / "dashboard.html"

class Handler(BaseHTTPRequestHandler):
    store = LeadStore()
    def respond(self, status, payload, content_type="application/json; charset=utf-8"):
        body = payload.encode() if isinstance(payload,str) else json.dumps(payload,ensure_ascii=False).encode()
        self.send_response(status); self.send_header("Content-Type",content_type); self.send_header("Content-Length",str(len(body))); self.send_header("X-Content-Type-Options","nosniff"); self.end_headers(); self.wfile.write(body)
    def do_GET(self):
        parsed=urlparse(self.path)
        if parsed.path=="/":
            if not DASHBOARD.exists(): return self.respond(404,{"error":"dashboard missing"})
            return self.respond(200,DASHBOARD.read_text(encoding="utf-8"),"text/html; charset=utf-8")
        if parsed.path=="/api/health": return self.respond(200,{"ok":True,"app":"Omarai","mode":"local"})
        if parsed.path=="/api/leads":
            q=parse_qs(parsed.query)
            try:
                limit=max(1,min(int(q.get("limit",["100"])[0]),500))
                leads=self.store.list(q.get("status",[None])[0],limit)
            except (ValueError,TypeError):
                return self.respond(400,{"error":"invalid status or limit"})
            return self.respond(200,{"leads":leads,"count":len(leads)})
        return self.respond(404,{"error":"not found"})
    def do_POST(self):
        try:
            size=int(self.headers.get("Content-Length","0"))
            if size>200_000: return self.respond(413,{"error":"request too large"})
            data=json.loads(self.rfile.read(size) or b"{}")
            if self.path=="/api/analyze": return self.respond(200,analyze(data.get("text",""),data.get("product_terms",[]),data.get("location_terms",[])))
            if self.path=="/api/leads":
                lead,created=self.store.add(data.get("text",""),data.get("source_url",""),data.get("platform","manual"),data.get("observed_at"),data.get("note",""),data.get("product_terms",[]),data.get("location_terms",[]))
                return self.respond(201 if created else 200,{"lead":lead,"created":created})
            if self.path.startswith("/api/leads/") and self.path.endswith("/status"):
                lead_id=self.path.split("/")[3]; lead=self.store.update_status(lead_id,data.get("status","new"))
                return self.respond(200,{"lead":lead}) if lead else self.respond(404,{"error":"lead not found"})
            return self.respond(404,{"error":"not found"})
        except (ValueError,TypeError,json.JSONDecodeError) as exc: return self.respond(400,{"error":str(exc)})
        except Exception: return self.respond(500,{"error":"internal server error"})
    def log_message(self,*args): pass

def serve(host="127.0.0.1",port=8765):
    if host not in ("127.0.0.1","localhost","::1"): raise ValueError("Omarai must bind to loopback unless authentication is added")
    server=ThreadingHTTPServer((host,port),Handler)
    print(f"Omarai running at http://{host}:{port} — Ctrl+C to stop")
    try: server.serve_forever()
    except KeyboardInterrupt: pass
    finally: server.server_close()

if __name__=="__main__": serve()
