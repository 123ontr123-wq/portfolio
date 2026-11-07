+++
title = "Hugo + GitHub Actions로 개인 포트폴리오 사이트 구축"
date = "2026-11-07"
description = "초급프로젝트 과제 1 — 개인 수행"
tags = ["Hugo", "GitHub Actions", "접근성"]
+++

## 개요 {#summary}

| 항목 | 내용 |
| --- | --- |
| 구분 | 2026학년도 초급프로젝트 과제 1 (수업 실습, **개인 수행**) |
| 기간 | 2026년 10월 ~ 2026년 11월 |
| 상태 | **완료** — 배포 후에도 내용 수정 시 자동 재배포로 계속 갱신 |
| 결과물 | 지금 보고 계신 이 사이트와 [GitHub 저장소](https://github.com/your-github-id/portfolio) |

## 목적 {#goal}

목표는 두 가지였습니다.

1. **나를 소개하는 공개 페이지 만들기** — 대학원 진학 준비 과정에서 관심 분야와 공부한 내용을 링크 하나로 보여 줄 곳이 필요했습니다.
2. **"내 PC에서만 되는" 상태 벗어나기** — 테마 ZIP을 받아 로컬에서 보는 것에 그치지 않고, `main`에 push하면 GitHub Actions가 빌드·배포까지 자동으로 처리하고, 저장소 이름이 들어간 하위 경로(`/portfolio/`)에서도 CSS·이미지·링크가 깨지지 않게 만드는 것이 해결하려던 문제였습니다.

## 내 역할 {#role}

개인 과제이므로 기획·설정·콘텐츠 작성·검증을 모두 직접 수행했습니다.

- 테마 선택과 수업 제공 스크립트 실행, Git 저장소 초기화·원격 연결·push
- `site/hugo.toml` 설정(언어, 메뉴, 소셜 링크, 아바타) 수정
- 소개·활동·학습 기록 글 작성
- 접근성·반응형 문제를 찾아 레이아웃 덮어쓰기(`site/layouts/`)와 CSS(`site/assets/css/custom.css`)로 수정
- 공개 사이트에서 데스크톱·모바일 폭과 키보드 조작 검증

AI(Claude)는 설정·코드 초안과 오류 분석에 활용했고, 적용 여부 판단과 공개 사이트에서의 확인은 제가 했습니다. 외부 테마는 [hugo-coder](https://github.com/luizdepra/hugo-coder)(MIT 라이선스)를 사용했습니다.

## 수행 과정과 선택 이유 {#process}

![push부터 공개까지의 배포 흐름: 로컬 수정 → git push(main) → GitHub Actions 빌드(Hugo 0.167.0) → GitHub Pages 배포 → 공개 사이트](../../images/deploy-flow.svg)

1. **테마 선택** — Hugo Themes에서 [hugo-coder](https://github.com/luizdepra/hugo-coder)를 골랐습니다. 
   - *선택 이유:* 자기소개 중심의 단순한 구조라 소개·활동을 찾기 쉽고, npm 빌드 같은 추가 의존성이 없어 Actions 빌드가 단순하며, 다크 모드·모바일 메뉴가 기본으로 들어 있습니다.
2. **배포 준비** — Download ZIP을 풀고 수업 제공 `prepare_github_pages.py`(3.1)를 실행해 `site/` 폴더와 `.github/workflows/hugo-pages.yml`을 만들었습니다. 워크플로는 Hugo 버전을 0.167.0으로 고정합니다.
3. **설정·콘텐츠 교체** — 데모 인물(John Doe)·예시 글·다국어 데모를 지우고 본인 정보로 바꿨습니다.
4. **검증과 개선** — 공개 사이트를 1440px·768px·390px 폭과 키보드만으로 점검하고, 발견한 문제를 고친 뒤 다시 push해 재배포를 확인했습니다.

## 산출물과 결과 {#result}

- **공개 사이트:** 이 사이트 자체입니다. `main`에 push하면 GitHub Actions가 빌드하고 GitHub Pages에 배포합니다.
- **소스 저장소:** [your-github-id/portfolio](https://github.com/your-github-id/portfolio) — 설정·콘텐츠·레이아웃 수정 이력을 커밋 단위로 확인할 수 있습니다.
- **배포 기록:** [Actions 실행 목록](https://github.com/your-github-id/portfolio/actions)에서 push마다 빌드·배포가 성공했는지 확인할 수 있습니다.
- **확인한 것:** 저장소 이름이 붙은 하위 경로에서도 홈·소개·활동 페이지를 주소창에 직접 입력해 열 수 있고, CSS·아바타·이 페이지의 흐름도 이미지가 정상적으로 불러와지는 것을 확인했습니다.
