# 장민성 포트폴리오 (Hugo + GitHub Pages)

2026학년도 초급프로젝트 과제 1로 만든 개인 소개 사이트입니다.

- 공개 사이트: https://your-github-id.github.io/portfolio/
- 테마: [hugo-coder](https://github.com/luizdepra/hugo-coder) (MIT) — 원본 테마 README는 [THEME-README.md](THEME-README.md)

> 처음 받은 경우 `python tools/set_github_id.py <GitHub아이디> [저장소이름]`으로 계정 주소를 반영합니다.

## 1. 필요한 도구와 버전

| 도구 | 버전 | 용도 |
| --- | --- | --- |
| Hugo **extended** | 0.167.0 | 사이트 빌드 (워크플로와 동일 버전 권장) |
| Dart Sass | 1.105.0 | 테마 SCSS 컴파일 (Actions에서 자동 설치) |
| Python | 3.9 이상 (Actions는 3.12) | `.github/pages_build.py` 실행 |
| Git | 2.x | 커밋·push |

설치 예시

- Windows: `winget install Hugo.Hugo.Extended` (설치 후 `hugo version`이 `+extended`로 표시되는지 확인)
- macOS: `brew install hugo`
- 정확한 버전이 필요하면 https://github.com/gohugoio/hugo/releases/tag/v0.167.0 에서 `hugo_extended_0.167.0_*` 파일을 받습니다.

## 2. 로컬에서 실행·빌드하기

```bash
# 저장소 받기
git clone https://github.com/your-github-id/portfolio.git
cd portfolio

# 개발 서버 (http://localhost:1313/portfolio/ 에서 확인)
cd site
hugo server --config hugo.toml,pages.json --theme template --themesDir themes

# 배포와 동일한 방식으로 빌드 (저장소 최상위에서 실행, 결과는 public/)
cd ..
python .github/pages_build.py --build
```

`public/`은 빌드 결과물이라 Git에 올리지 않습니다(`.gitignore`).

## 3. 어디를 고치면 되나

| 바꾸고 싶은 것 | 파일 |
| --- | --- |
| 사이트 제목·이름·소개 문구·메뉴·GitHub 링크 | `site/hugo.toml` |
| 소개 페이지 | `site/content/about.md` |
| 활동 목록 / 대표 활동 | `site/content/projects/` |
| 학습 기록 글 | `site/content/posts/` |
| 아바타·이미지 | `site/static/images/` |
| 추가 CSS | `site/assets/css/custom.css` |
| 테마 템플릿 덮어쓰기(메뉴 버튼·다크 모드 버튼·푸터·아바타) | `site/layouts/_partials/` |
| 배포 주소(baseURL) | `site/pages.json` (Actions에서는 Pages 주소가 자동 적용) |

원본 테마(`site/themes/template/`)는 직접 수정하지 않습니다.

## 4. 수정 후 재배포와 확인

1. 파일을 수정한 뒤 커밋하고 `main`에 push합니다.
   ```bash
   git add -A
   git commit -m "content: 소개 문구 수정"
   git push origin main
   ```
2. GitHub 저장소의 **Actions** 탭 → `Deploy Hugo to GitHub Pages` 실행이 자동으로 시작되는지 확인합니다. `build`와 `deploy`가 모두 초록색(성공)이어야 합니다.
3. 실행 요약의 `deploy` 단계에 표시된 주소(https://your-github-id.github.io/portfolio/)를 열고, 브라우저 캐시를 피하려면 시크릿 창에서 바뀐 내용을 확인합니다.

처음 한 번은 **Settings → Pages → Build and deployment → Source**를 **GitHub Actions**로 설정해야 합니다. 설정 전에 실패한 실행은 *Re-run all jobs*로 다시 실행합니다.

## 5. 출처와 이용 조건

| 자료 | 사용 위치 | 구분 | 출처·조건 |
| --- | --- | --- | --- |
| hugo-coder 테마 | `site/themes/template/` 전체 | 외부 자료 | https://github.com/luizdepra/hugo-coder · MIT 라이선스 (`LICENSE.md` 유지, 푸터에 고지) |
| Font Awesome 아이콘·글꼴 | 테마에 포함 | 외부 자료 | 테마 동봉 · Font Awesome Free 라이선스 (아이콘 CC BY 4.0, 글꼴 SIL OFL 1.1) |
| `prepare_github_pages.py` → `.github/pages_build.py`, 워크플로 | `.github/` | 수업 제공 | 초급프로젝트 수업 자료 |
| 아바타 `avatar.svg`, 배포 흐름도 `deploy-flow.svg` | `site/static/images/` | 직접 제작 (AI 도움으로 SVG 코드 작성) | — |
| 소개·활동·학습 기록 글 | `site/content/` | 직접 작성 (AI로 문장 초안·정리) | — |
| 추가 CSS·레이아웃 덮어쓰기 | `site/assets/`, `site/layouts/` | 직접 수정 (AI로 코드 초안 작성, 직접 검증) | 원본 테마 파일을 복사해 수정 (MIT) |

AI 도구: Claude (Anthropic) — 설정·코드 초안, 오류 분석, 문장 정리에 사용했습니다.
