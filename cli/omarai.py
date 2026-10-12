"""Command-line interface for Omarai."""
import argparse
import json

from agents.omarai import LeadStore, analyze
from api.omarai import serve

def main():
    parser=argparse.ArgumentParser(prog="omarai",description="Arabic lead-intent helper")
    sub=parser.add_subparsers(dest="command",required=True)
    p=sub.add_parser("analyze"); p.add_argument("--text",required=True); p.add_argument("--product",default=""); p.add_argument("--location",default="")
    p=sub.add_parser("serve"); p.add_argument("--host",default="127.0.0.1"); p.add_argument("--port",type=int,default=8765)
    p=sub.add_parser("import-csv"); p.add_argument("--file",required=True)
    p=sub.add_parser("list"); p.add_argument("--limit",type=int,default=100); p.add_argument("--status")
    p=sub.add_parser("export-csv"); p.add_argument("--file",required=True)
    args=parser.parse_args()
    if args.command=="analyze":
        result=analyze(args.text,[x.strip() for x in args.product.split(",") if x.strip()],[x.strip() for x in args.location.split(",") if x.strip()])
        print(json.dumps(result,ensure_ascii=False,indent=2)); return
    store=LeadStore()
    if args.command=="serve": serve(args.host,args.port)
    elif args.command=="import-csv": print(json.dumps(store.import_csv(args.file),ensure_ascii=False,indent=2))
    elif args.command=="list": print(json.dumps(store.list(args.status,args.limit),ensure_ascii=False,indent=2))
    elif args.command=="export-csv": print(f"Exported {store.export_csv(args.file)} leads to {args.file}")
if __name__=="__main__": main()
