+++
title = "Hugo 사이트 구조 정리: content, layouts, static"
date = "2026-11-07T20:00:00+09:00"
tags = ["Hugo"]
+++

포트폴리오를 만들면서 Hugo 폴더 역할을 정리했습니다.

| 폴더 | 역할 | 이 사이트에서 한 일 |
| --- | --- | --- |
| `site/content/` | 글(Markdown) | 소개·활동·학습 기록 작성 |
| `site/layouts/` | 테마 템플릿 덮어쓰기 | 메뉴 버튼·다크 모드 버튼 접근성 수정 |
| `site/static/` | 그대로 복사되는 파일 | 아바타·흐름도 SVG |
| `site/assets/` | Hugo가 처리하는 파일 | 추가 CSS(`css/custom.css`) |
| `site/themes/template/` | 원본 테마 | 직접 수정하지 않고 위 폴더에서 덮어씀 |

테마 원본을 직접 고치지 않고 `site/layouts/`에 같은 경로의 파일을 두면 그 파일이 우선 적용됩니다.
나중에 테마를 업데이트해도 내 수정이 어디 있는지 분명하다는 것이 장점이었습니다.
