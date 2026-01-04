# FSD Dependency Rules Reference

## 핵심 원칙

FSD의 의존성 규칙은 코드의 예측 가능성과 유지보수성을 보장합니다.

## 레이어 간 의존성

### 규칙 1: 상위에서 하위로만 Import

```
app → pages → widgets → features → entities → shared
```

```typescript
// ✅ 올바른 의존성 방향

// pages/home/ui/HomePage.tsx
import { Header } from '@/widgets/header';
import { ProductList } from '@/widgets/product-list';
import { useAuth } from '@/features/auth';
import { ProductCard } from '@/entities/product';
import { Button } from '@/shared/ui';

// ❌ 잘못된 의존성 방향

// entities/user/ui/UserCard.tsx
import { LoginButton } from '@/features/auth';  // 금지! (하위→상위)

// shared/ui/Button.tsx
import { useAuth } from '@/features/auth';      // 금지! (하위→상위)
```

### 규칙 2: 같은 레이어 슬라이스 간 Import 금지

```typescript
// ❌ 금지: features 내 슬라이스 간 import
// features/checkout/ui/CheckoutForm.tsx
import { useAuth } from '@/features/auth';

// ❌ 금지: entities 내 슬라이스 간 import
// entities/order/model/orderStore.ts
import { Product } from '@/entities/product';
```

## 문제 해결 패턴

### 패턴 1: 상위 레이어에서 조합

슬라이스 간 연결이 필요할 때, 상위 레이어에서 조합합니다.

```typescript
// 문제: add-to-cart 기능에서 user 정보 필요

// ❌ 잘못된 방법
// features/add-to-cart/ui/AddToCartButton.tsx
import { useUser } from '@/entities/user';  // 같은 레벨 entities는 OK

// ✅ 올바른 방법: widgets에서 조합
// widgets/product-card/ui/ProductCard.tsx
import { AddToCartButton } from '@/features/add-to-cart';
import { useAuth } from '@/features/auth';

function ProductCard({ product }: Props) {
  const { isAuthenticated } = useAuth();

  return (
    <div>
      <ProductInfo product={product} />
      <AddToCartButton
        productId={product.id}
        disabled={!isAuthenticated}
      />
    </div>
  );
}
```

### 패턴 2: Props/Callbacks로 의존성 주입

```typescript
// features/add-to-cart/ui/AddToCartButton.tsx
interface Props {
  productId: string;
  userId?: string;           // 외부에서 주입
  onAuthRequired?: () => void; // 콜백으로 처리
}

export function AddToCartButton({ productId, userId, onAuthRequired }: Props) {
  const handleClick = () => {
    if (!userId) {
      onAuthRequired?.();
      return;
    }
    addToCart(productId, userId);
  };

  return <Button onClick={handleClick}>장바구니 담기</Button>;
}
```

### 패턴 3: Cross-import API 사용 (고급)

FSD는 `@x` 표기법을 통한 제한적 cross-import를 허용합니다:

```
entities/
├── user/
│   └── @x/              # Cross-import용 API
│       └── product.ts   # product 슬라이스에만 공개
└── product/
    └── model/
        └── useProductWithUser.ts
```

```typescript
// entities/user/@x/product.ts
export { useUserById } from '../model';

// entities/product/model/useProductWithUser.ts
import { useUserById } from '@/entities/user/@x/product';
```

**주의:** Cross-import는 최후의 수단으로만 사용하세요.

### 패턴 4: 공통 로직은 Shared로

여러 슬라이스에서 사용하는 로직은 shared로 이동:

```typescript
// ❌ features/auth에 있던 validateEmail
// features/auth/lib/validateEmail.ts

// ✅ shared로 이동
// shared/lib/validation/email.ts
export function validateEmail(email: string): boolean {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}
```

## 의존성 검사

### ESLint 규칙 (Steiger)

```javascript
// .eslintrc.js
module.exports = {
  plugins: ['@feature-sliced/eslint-plugin'],
  rules: {
    '@feature-sliced/layers-slices': 'error',
    '@feature-sliced/public-api': 'error',
    '@feature-sliced/absolute-relative': 'error',
  },
};
```

### Import 패턴

```typescript
// ✅ 올바른 import 경로
import { Button } from '@/shared/ui';
import { UserCard } from '@/entities/user';
import { LoginForm } from '@/features/auth';

// ❌ 슬라이스 내부 직접 접근 금지
import { Button } from '@/shared/ui/Button/Button';
import { UserCard } from '@/entities/user/ui/UserCard';
```

## 의존성 시각화

```
┌─────────────────────────────────────────────────────────┐
│                         app                              │
├─────────────────────────────────────────────────────────┤
│                        pages                             │
│   ┌─────────┐  ┌─────────┐  ┌─────────┐                 │
│   │  home   │  │ product │  │  cart   │                 │
│   └────┬────┘  └────┬────┘  └────┬────┘                 │
├────────┼────────────┼───────────┼───────────────────────┤
│        │          widgets       │                        │
│   ┌────▼────┐  ┌─────────┐  ┌──▼──────┐                 │
│   │ header  │  │ sidebar │  │cart-list│                 │
│   └────┬────┘  └────┬────┘  └────┬────┘                 │
├────────┼────────────┼───────────┼───────────────────────┤
│        │         features       │                        │
│   ┌────▼────┐  ┌────▼────┐  ┌──▼──────┐                 │
│   │  auth   │  │ search  │  │add-cart │   ← 서로 금지    │
│   └────┬────┘  └────┬────┘  └────┬────┘                 │
├────────┼────────────┼───────────┼───────────────────────┤
│        │         entities       │                        │
│   ┌────▼────┐  ┌────▼────┐  ┌──▼──────┐                 │
│   │  user   │  │ product │  │  cart   │   ← 서로 금지    │
│   └────┬────┘  └────┬────┘  └────┬────┘                 │
├────────┼────────────┼───────────┼───────────────────────┤
│        └────────────┴───────────┘                        │
│                       shared                             │
│              (ui, api, lib, config)                      │
└─────────────────────────────────────────────────────────┘
```
