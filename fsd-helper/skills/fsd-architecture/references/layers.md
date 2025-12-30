# FSD Layers Reference

## 레이어 개요

FSD는 7개의 표준화된 레이어를 정의하며, 각 레이어는 특정 책임을 가집니다.

## 레이어 상세

### 1. App Layer

애플리케이션의 진입점과 전역 설정을 담당합니다.

```
src/app/
├── providers/          # Context Providers (Theme, Auth, Store)
├── routes/             # 라우팅 설정
├── styles/             # 전역 스타일
├── index.tsx           # 애플리케이션 진입점
└── App.tsx
```

**포함 요소:**
- 라우팅 설정 (React Router, Next.js 라우팅)
- 전역 프로바이더 (Redux, React Query, Theme)
- 전역 스타일 및 CSS 리셋
- 에러 바운더리

### 2. Pages Layer

라우트에 대응하는 페이지 컴포넌트입니다.

```
src/pages/
├── home/
│   ├── ui/
│   │   └── HomePage.tsx
│   └── index.ts
├── article/
│   ├── ui/
│   │   └── ArticlePage.tsx
│   ├── api/
│   │   └── getArticle.ts
│   └── index.ts
└── settings/
    └── ...
```

**역할:**
- 위젯과 피처를 조합하여 페이지 구성
- 페이지별 데이터 페칭 로직
- 레이아웃 적용

### 3. Widgets Layer

독립적으로 동작하는 대규모 UI 블록입니다.

```
src/widgets/
├── header/
│   ├── ui/
│   │   ├── Header.tsx
│   │   └── Navigation.tsx
│   └── index.ts
├── sidebar/
│   └── ...
└── article-card/
    └── ...
```

**특징:**
- 여러 엔티티와 피처를 조합
- 재사용 가능한 독립적 UI 블록
- 자체적인 비즈니스 로직 포함 가능

### 4. Features Layer

사용자에게 비즈니스 가치를 제공하는 기능 단위입니다.

```
src/features/
├── auth/
│   ├── ui/
│   │   ├── LoginForm.tsx
│   │   └── LogoutButton.tsx
│   ├── api/
│   │   └── login.ts
│   ├── model/
│   │   └── authStore.ts
│   └── index.ts
├── add-to-cart/
│   └── ...
└── toggle-theme/
    └── ...
```

**포함 요소:**
- 사용자 액션 처리 (로그인, 장바구니 추가)
- 해당 기능에 필요한 UI, API, 상태

### 5. Entities Layer

프로젝트가 다루는 비즈니스 엔티티입니다.

```
src/entities/
├── user/
│   ├── ui/
│   │   ├── UserAvatar.tsx
│   │   └── UserCard.tsx
│   ├── model/
│   │   ├── types.ts
│   │   └── userStore.ts
│   ├── api/
│   │   └── getUser.ts
│   └── index.ts
├── product/
│   └── ...
└── order/
    └── ...
```

**특징:**
- 도메인 모델 정의 (User, Product, Order)
- 엔티티 관련 UI 컴포넌트
- CRUD 작업

### 6. Shared Layer

모든 레이어에서 재사용되는 코드입니다.

```
src/shared/
├── ui/
│   ├── Button/
│   ├── Input/
│   ├── Modal/
│   └── index.ts
├── api/
│   ├── client.ts
│   └── types.ts
├── lib/
│   ├── formatDate.ts
│   └── cn.ts
├── config/
│   └── constants.ts
└── types/
    └── common.ts
```

**포함 요소:**
- UI 키트 (Button, Input, Modal 등)
- API 클라이언트 설정
- 유틸리티 함수
- 타입 정의
- 상수값

## 레이어별 Import 규칙

```typescript
// ✅ 올바른 import (상위 → 하위)
// pages/home/ui/HomePage.tsx
import { Header } from '@/widgets/header';
import { LoginButton } from '@/features/auth';
import { UserCard } from '@/entities/user';
import { Button } from '@/shared/ui';

// ❌ 잘못된 import (하위 → 상위)
// entities/user/ui/UserCard.tsx
import { LoginButton } from '@/features/auth';  // 금지!
```
