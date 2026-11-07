#!/usr/bin/env python3
"""자리표시자 your-github-id/portfolio 를 실제 GitHub 계정·저장소 이름으로 바꿉니다.

사용법 (저장소 최상위 폴더에서):
    python tools/set_github_id.py 내아이디            # 저장소 이름이 portfolio 인 경우
    python tools/set_github_id.py 내아이디 저장소이름
이후 prepare_github_pages.py 를 다시 실행해 site/pages.json 의 baseURL 도 갱신합니다.
"""
import re, subprocess, sys
from pathlib import Path

if len(sys.argv) not in (2, 3) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]{0,38}', sys.argv[1]):
    sys.exit(__doc__)
owner = sys.argv[1]
repo = sys.argv[2] if len(sys.argv) == 3 else 'portfolio'
user_site = repo.lower() == owner.lower() + '.github.io'
page = f'https://{owner.lower()}.github.io/' + ('' if user_site else repo + '/')
root = Path(__file__).resolve().parent.parent
targets = [root / 'README.md', root / 'site/hugo.toml'] + list((root / 'site/content').rglob('*.md'))
for f in targets:
    t = f.read_text(encoding='utf-8')
    n = t.replace('https://your-github-id.github.io/portfolio/', page)
    n = n.replace('your-github-id/portfolio', f'{owner}/{repo}')
    n = n.replace('your-github-id', owner)
    if n != t:
        f.write_text(n, encoding='utf-8')
        print('수정:', f.relative_to(root))
subprocess.run([sys.executable, 'prepare_github_pages.py'], cwd=root,
               input=f'https://github.com/{owner}/{repo}\n', text=True, check=True)
print('완료. git diff 로 확인한 뒤 커밋하세요.')
