"""Validate local documentation without network access or dependencies."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def main():
    required = ['AGENTS.md', 'ARCHITECTURE.md', 'docs/PLANS.md',
                'docs/exec-plans/active', 'docs/exec-plans/completed',
                'src/agent_learning', 'tests', 'evals']
    stages = ['01_python', '02_llm_api', '03_function_calling', '04_langchain',
              '05_langgraph', '06_rag', '07_mcp', '08_fastapi', '09_docker']
    required.extend(f'labs/{stage}/README.md' for stage in stages)
    errors = [f'Missing path: {p}' for p in required if not (ROOT / p).exists()]
    documents = [ROOT / p for p in ('README.md', 'AGENTS.md', 'ARCHITECTURE.md')]
    for folder in ('docs', 'labs', 'src', 'tests', 'evals'):
        documents.extend(sorted((ROOT / folder).rglob('*.md')))
    for document in documents:
        if not document.exists():
            errors.append(f'Missing document: {document}')
            continue
        content = document.read_text(encoding='utf-8')
        if '\ufffd' in content or re.search(r'\?{4,}', content):
            errors.append(f'Possible encoding damage: {document.relative_to(ROOT)}')
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', content):
            target = target.strip().strip('<>')
            if urlsplit(target).scheme or target.startswith('#'):
                continue
            local = unquote(target.split('#', 1)[0])
            if not (document.parent / local).exists():
                errors.append(f'Broken link in {document.relative_to(ROOT)}: {target}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'OK: {len(documents)} Markdown files; local links, encoding and structure checked.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
