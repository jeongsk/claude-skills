# FSD Migration Guide

## 마이그레이션 개요

기존 프로젝트를 FSD로 마이그레이션하는 전략입니다.

## 단계별 마이그레이션

### Phase 1: Shared와 App 레이어 정리

가장 먼저 양 끝단 레이어를 정리합니다.

```
기존 구조:
src/
├── components/
│   ├── Button.tsx
│   ├── Input.tsx
│   └── Modal.tsx
├── utils/
│   └── formatDate.ts
├── api/
│   └── client.ts
└── App.tsx

Phase 1 후:
src/
├── app/
│   ├── App.tsx
│   ├── providers/
│   └── routes/
├── shared/
│   ├── ui/
│   │   ├── Button/
│   │   ├── Input/
│   │   └── Modal/
│   ├── lib/
│   │   └── formatDate.ts
│   └── api/
│       └── client.ts
└── components/     # 아직 정리 안 된 컴포넌트들
```

### Phase 2: Pages 레이어 분리

라우트에 대응하는 페이지 컴포넌트를 분리합니다.

```
Phase 2 후:
src/
├── app/
├── pages/
│   ├── home/
│   │   └── ui/
│   │       └── HomePage.tsx
│   ├── product/
│   │   └── ui/
│   │       └── ProductPage.tsx
│   └── cart/
│       └── ui/
│           └── CartPage.tsx
├── shared/
└── components/     # 여전히 정리 필요
```

### Phase 3: Entities 식별 및 분리

비즈니스 엔티티를 식별하고 분리합니다.

```
Phase 3 후:
src/
├── app/
├── pages/
├── entities/
│   ├── user/
│   │   ├── ui/
│   │   │   └── UserCard.tsx
│   │   ├── model/
│   │   │   └── types.ts
│   │   └── index.ts
│   ├── product/
│   │   ├── ui/
│   │   │   └── ProductCard.tsx
│   │   ├── model/
│   │   └── index.ts
│   └── cart/
├── shared/
└── components/     # 점점 줄어듦
```

### Phase 4: Features 분리

사용자 액션 기반 기능을 분리합니다.

```
Phase 4 후:
src/
├── app/
├── pages/
├── features/
│   ├── auth/
│   │   ├── ui/
│   │   │   ├── LoginForm.tsx
│   │   │   └── LogoutButton.tsx
│   │   ├── api/
│   │   ├── model/
│   │   └── index.ts
│   ├── add-to-cart/
│   └── checkout/
├── entities/
├── shared/
└── components/     # 거의 비어감
```

### Phase 5: Widgets 조합

독립적인 UI 블록을 widgets로 조합합니다.

```
Phase 5 후:
src/
├── app/
├── pages/
├── widgets/
│   ├── header/
│   ├── sidebar/
│   ├── product-list/
│   └── cart-summary/
├── features/
├── entities/
└── shared/
```

## Import 경로 마이그레이션

### Path Aliases 설정

```json
// tsconfig.json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@/app/*": ["src/app/*"],
      "@/pages/*": ["src/pages/*"],
      "@/widgets/*": ["src/widgets/*"],
      "@/features/*": ["src/features/*"],
      "@/entities/*": ["src/entities/*"],
      "@/shared/*": ["src/shared/*"]
    }
  }
}
```

### Import 경로 변환

```typescript
// Before
import { Button } from '../../../components/Button';
import { formatDate } from '../../utils/formatDate';

// After
import { Button } from '@/shared/ui';
import { formatDate } from '@/shared/lib';
```

## 마이그레이션 체크리스트

### Phase 1: Shared & App
- [ ] 전역 UI 컴포넌트를 `shared/ui`로 이동
- [ ] 유틸리티 함수를 `shared/lib`로 이동
- [ ] API 클라이언트를 `shared/api`로 이동
- [ ] 앱 진입점을 `app`으로 구성
- [ ] 라우팅 설정을 `app/routes`로 이동

### Phase 2: Pages
- [ ] 라우트별 페이지 컴포넌트 식별
- [ ] 각 페이지를 `pages/{name}/ui`로 이동
- [ ] 페이지별 index.ts 작성

### Phase 3: Entities
- [ ] 비즈니스 엔티티 식별 (User, Product 등)
- [ ] 엔티티별 타입 정의를 `model/types.ts`로 이동
- [ ] 엔티티 UI를 `ui`로 이동
- [ ] Public API 작성

### Phase 4: Features
- [ ] 사용자 액션 기반 기능 식별
- [ ] 각 기능을 독립 슬라이스로 분리
- [ ] 기능별 상태 관리 정리

### Phase 5: Widgets
- [ ] 재사용 가능한 UI 블록 식별
- [ ] Features와 Entities 조합하여 Widgets 구성

## 점진적 마이그레이션 팁

### 1. 새 기능부터 FSD 적용

```
src/
├── legacy/          # 기존 코드
│   └── components/
├── app/             # 새 FSD 구조
├── pages/
├── features/
│   └── new-feature/ # 새 기능은 FSD로
├── entities/
└── shared/
```

### 2. Barrel Export로 호환성 유지

```typescript
// legacy/components/index.ts
// 기존 import 경로 호환
export { Button } from '@/shared/ui';
export { formatDate } from '@/shared/lib';
```

### 3. ESLint로 규칙 강제

```javascript
// .eslintrc.js
module.exports = {
  rules: {
    'no-restricted-imports': [
      'error',
      {
        patterns: [
          {
            group: ['@/features/*/*', '@/entities/*/*'],
            message: 'Use public API (index.ts) instead',
          },
        ],
      },
    ],
  },
};
```

## 마이그레이션 도구

### Steiger

FSD 규칙 검사 도구:

```bash
npx steiger ./src
```

### 자동화 스크립트 예시

```bash
#!/bin/bash
# create-slice.sh

LAYER=$1
NAME=$2

mkdir -p "src/$LAYER/$NAME"/{ui,model,api,lib}
touch "src/$LAYER/$NAME/index.ts"

echo "export {};" > "src/$LAYER/$NAME/index.ts"
echo "Created slice: src/$LAYER/$NAME"
```
