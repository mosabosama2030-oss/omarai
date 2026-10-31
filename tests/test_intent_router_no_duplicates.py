"""Regression test to prevent duplicate symbol definitions in intent_router."""
import ast
import pathlib


def test_no_duplicate_followup_symbols():
    """Ensure followup lead-in symbols are defined only once."""
    path = pathlib.Path(__file__).parent.parent / "agents" / "intent_router.py"
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    
    names = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in {
                    "_FOLLOWUP_LEAD_IN_RE",
                    "_FOLLOWUP_ASPECT_FRAGMENTS",
                }:
                    names.append(target.id)
        elif isinstance(node, ast.FunctionDef) and node.name == "_strip_followup_leadin":
            names.append(node.name)
    
    counts = {name: names.count(name) for name in set(names)}
    assert counts.get("_FOLLOWUP_LEAD_IN_RE", 0) == 1, "Duplicate _FOLLOWUP_LEAD_IN_RE"
    assert counts.get("_FOLLOWUP_ASPECT_FRAGMENTS", 0) == 1, "Duplicate _FOLLOWUP_ASPECT_FRAGMENTS"
    assert counts.get("_strip_followup_leadin", 0) == 1, "Duplicate _strip_followup_leadin"
