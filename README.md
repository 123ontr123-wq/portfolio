# 장민성 포트폴리오 (Hugo + GitHub Pages)

2026학년도 초급프로젝트 과제 1로 만든 개인 소개 사이트입니다.

- 공개 사이트: https://your-github-id.github.io/portfolio/
- 테마: [hugo-coder](https://github.com/luizdepra/hugo-coder) (MIT) — 원본 테마 README는 [THEME-README.md](THEME-README.md)

## 1. 필요한 도구와 버전 {#tools}

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
