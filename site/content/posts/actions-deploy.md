+++
title = "GitHub Actions로 Hugo 배포하기: push에서 공개까지"
date = "2026-11-07T21:00:00+09:00"
tags = ["GitHub Actions", "배포"]
+++

워크플로 파일은 `.github/workflows/hugo-pages.yml`입니다. 흐름은 다음과 같습니다.

1. `main` 브랜치에 push하면 워크플로가 자동으로 시작됩니다(`on: push: branches: [main]`).
2. build 작업이 Hugo **0.167.0** extended와 Dart Sass를 설치합니다. 버전을 고정해 두어 PC와 서버의 결과가 달라지지 않게 합니다.
3. `actions/configure-pages`가 알려 준 실제 주소(`base_url`)를 `--baseURL`로 넘겨 빌드합니다. 그래서 설정 파일에 데모 주소가 남아 있어도 배포 결과는 내 저장소 주소를 따릅니다.
4. 빌드 결과(`public/`)를 업로드하고 deploy 작업이 GitHub Pages에 배포합니다.

처음에 저장소 **Settings → Pages → Source**를 *GitHub Actions*로 바꾸지 않으면 deploy 단계가 실패합니다. 설정 후 실패한 실행을 다시 실행(Re-run)하면 됩니다.
