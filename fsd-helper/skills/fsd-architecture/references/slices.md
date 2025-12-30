# FSD Slices Reference

## 슬라이스 개요

슬라이스는 레이어 내에서 비즈니스 도메인별로 코드를 분할하는 단위입니다.

## 슬라이스 네이밍 규칙

### 좋은 슬라이스 이름

```
features/
├── auth/              # 인증 기능
├── add-to-cart/       # 장바구니 추가
├── toggle-theme/      # 테마 전환
├── send-comment/      # 댓글 작성
└── like-article/      # 글 좋아요
```

**특징:**
- 동사 + 명사 형태 (기능의 목적 명확)
- kebab-case 사용
- 비즈니스 용어 사용

### 피해야 할 이름

```
features/
├── utils/             # ❌ 너무 일반적
├── helpers/           # ❌ shared에 있어야 함
├── components/        # ❌ 역할 불명확
└── common/            # ❌ shared 사용
```

## 슬라이스 구조

### 기본 구조

```
features/auth/
├── ui/
│   ├── LoginForm.tsx
│   ├── LoginForm.module.css
│   └── index.ts
├── api/
│   ├── login.ts
│   ├── logout.ts
│   └── index.ts
├── model/
│   ├── types.ts
│   ├── authStore.ts
│   └── index.ts
├── lib/
│   └── validateCredentials.ts
└── index.ts            # Public API
```

### Public API (index.ts)

각 슬라이스는 `index.ts`를 통해 공개 API를 정의합니다:

```typescript
// features/auth/index.ts
export { LoginForm } from './ui';
export { login, logout } from './api';
export { useAuth, authStore } from './model';
export type { User, AuthState } from './model/types';
```

**중요:** 다른 슬라이스에서는 반드시 `index.ts`를 통해서만 import해야 합니다.

```typescript
// ✅ 올바른 import
import { LoginForm } from '@/features/auth';

// ❌ 잘못된 import (내부 구조에 직접 접근)
import { LoginForm } from '@/features/auth/ui/LoginForm';
```

## 슬라이스 간 관계

### 같은 레이어 내 슬라이스

**원칙:** 같은 레이어의 슬라이스끼리는 서로 import할 수 없습니다.

```typescript
// features/add-to-cart/ui/AddToCartButton.tsx

// ❌ 금지: 같은 레이어 슬라이스 import
import { useAuth } from '@/features/auth';

// ✅ 해결책 1: 상위 레이어에서 조합
// widgets/product-card/ui/ProductCard.tsx
import { AddToCartButton } from '@/features/add-to-cart';
import { useAuth } from '@/features/auth';

// ✅ 해결책 2: 하위 레이어로 공통 로직 이동
import { useCurrentUser } from '@/entities/user';
```

### Cross-import가 필요한 경우

슬라이스 간 의존성이 필요할 때의 패턴:

```typescript
// 1. Composition in Widgets
// widgets/header/ui/Header.tsx
import { UserMenu } from '@/features/user-menu';
import { ThemeToggle } from '@/features/toggle-theme';
import { SearchBar } from '@/features/search';

// 2. Props/Callbacks로 전달
// features/add-to-cart/ui/AddToCartButton.tsx
interface Props {
  productId: string;
  onAuthRequired?: () => void;  // 상위에서 주입
}

// 3. Shared Events/Store
// shared/lib/events.ts
export const authEvents = createEventEmitter<AuthEvents>();
```

## 슬라이스 예시

### Entities 레이어

```
entities/
├── user/              # 사용자
├── product/           # 상품
├── order/             # 주문
├── cart/              # 장바구니
├── article/           # 게시글
└── comment/           # 댓글
```

### Features 레이어

```
features/
├── auth/              # 로그인/로그아웃
├── add-to-cart/       # 장바구니 추가
├── checkout/          # 결제
├── write-review/      # 리뷰 작성
├── search-products/   # 상품 검색
└── filter-products/   # 상품 필터링
```

### Pages 레이어

```
pages/
├── home/              # 메인 페이지
├── catalog/           # 상품 목록
├── product-detail/    # 상품 상세
├── cart/              # 장바구니
├── checkout/          # 결제
├── profile/           # 프로필
└── settings/          # 설정
```
