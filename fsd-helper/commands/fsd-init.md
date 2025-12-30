---
description: Initialize FSD folder structure in project
arguments:
  - name: framework
    description: "Framework type (react, next, vite)"
    required: false
    default: "react"
  - name: src
    description: "Source directory path"
    required: false
    default: "src"
---

# FSD Init Command

새 프로젝트에 Feature-Sliced Design 폴더 구조를 초기화합니다.

## Task

1. 현재 프로젝트 구조를 분석하여 기존 `src` 폴더 존재 여부 확인
2. 프레임워크에 맞는 FSD 구조 생성:

### 기본 구조 생성

```
{src}/
├── app/
│   ├── providers/
│   ├── routes/
│   └── styles/
├── pages/
├── widgets/
├── features/
├── entities/
└── shared/
    ├── ui/
    ├── api/
    ├── lib/
    ├── config/
    └── types/
```

3. 각 레이어에 기본 `index.ts` 파일 생성
4. `tsconfig.json`에 path aliases 추가 (존재하는 경우)

### Path Aliases 설정

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["{src}/*"],
      "@/app/*": ["{src}/app/*"],
      "@/pages/*": ["{src}/pages/*"],
      "@/widgets/*": ["{src}/widgets/*"],
      "@/features/*": ["{src}/features/*"],
      "@/entities/*": ["{src}/entities/*"],
      "@/shared/*": ["{src}/shared/*"]
    }
  }
}
```

### Framework별 추가 설정

**Next.js:**
- `app/` 디렉토리가 이미 존재하면 FSD의 app 레이어는 `_app` 또는 `layout.tsx`로 통합
- Next.js App Router 사용 시 라우팅은 Next.js 방식 유지

**Vite:**
- `vite.config.ts`에 alias 설정 추가

5. `.eslintrc`에 FSD import 규칙 추가 권장사항 안내

## Output

- 생성된 폴더 구조 트리 출력
- 추가 설정 필요 사항 안내
- 다음 단계 가이드 (슬라이스 생성 방법)
