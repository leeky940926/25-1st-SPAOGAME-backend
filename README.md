# SPAO Clone Project

- Trends meet Basic Be Transic! - 스파오(SPAO) 사이트 클론.

## 🎇 팀명 : SPAOGAME - 스파오게임

- 팀원들 각자의 기술에 익숙해지는 것을 목표로 하여, 페이지 단위로 개발.
- 팀원들 수준별로 적절한 역할 분담과 애자일한 스크럼 방식의 미팅, 그리고 규칙적이고 능동적인 의사소통으로 프로젝트를 성공적으로 마무리.
- 기획 과정 없이 짧은 기간 안에 기술 습득 및 기본 기능 구현에 집중하기 위해서 SPAO 사이트를 참고.

## 📅 개발 기간 및 개발 인원

- 개발 기간 : 2021-10-05 ~ 2021-10-15 (공휴일 포함)
- 개발 인원 <br/>
 👨‍👧‍👦 **Front-End** 3명 : [강성구](https://github.com/seonggookang), [김현진](https://github.com/71summernight), [정경훈](https://github.com/kyunghoon1017) <br/>
 👨‍👧‍👦 **Back-End** 3명 : [김주현](https://github.com/kjhabc2002), [이기용](https://github.com/leeky940926), [송영록](https://github.com/crescentfull)

## 🎬 프로젝트 구현 영상

- 🔗 [영상 링크]

## ⚙ 적용 기술
- **Front-End** : HTML5, CSS3, React, SASS, JSX
- **Back-End** : Python, Django, MySQL, jwt, bcypt, AWS RDS, AWS EC2
- **Common** : Git, Github, Slack, Trello, Postman or Insomnia

## 🗜 [데이터베이스 Diagram](https://www.erdcloud.com/d/m3PMPFjJyi8rAWYGK)
![SPAO_diagram_final](https://user-images.githubusercontent.com/78721108/137625673-58007c42-c404-4489-be98-d9a47b6dfe4d.png)

## 💻 구현 기능

#### 김주현

- 상품상세페이지 후기 및 댓글 등록 기능 구현
- 메인페이지 검색기능 구현

#### 이기용

- 상품 목록 조회 API
- 상품 상세 조회 API
- 상품 조건식 정렬 API

#### 송영록

- 회원가입 API
- 로그인 API
- 장바구니 상품 추가, 수정, 삭제 API

#### 김현진
- 상품리스트 레이아웃 구현
- 페이지네이션으로 상품데이터를 받아오는 기능
- 높은가격순, 낮은가격순,이름순,최신등록순,컬러순 ordering 기능
- 상세페이지의 레이아웃 구현
- query string url 을 사용한 상세페이지 연결 구현
- fetch post로 장바구니페이지에 데이터 전달 기능
- review form 레이아웃 구현
- fetch get/delete를 통한 후기 게시글, 댓글 등록/삭제 기능


## ⌨ EndPoint

- POST/users/signup (회원가입)
- POST/users/signin (로그인)
- POST/orders/cart (장바구니 생성)
- GET/orders/cart (장바구니 조회)
- PATCH/orders/cart (장바구니 수정)
- DEL/orders/cart (장바구니 삭제)
- POST/postings  (후기 등록)
- POST/postings/comments (댓글 등록)
- POST/postings/int:comment_id (댓글 삭제)

- POST/products/menus (메뉴 항목 추가)
- GET/products/menus (메뉴 항목 리스트 조회)
- POST/products/categories (카테고리 항목 추가)
- GET/products/menus/menu_name (특정 메뉴별 카테고리 항목 리스트 조회)
- POST/products (상품 등록)
- GET/products/menu_name/category_name (특정 메뉴-카테고리별 상품 리스트 조회)
- GET/products/product_id (특정 상품에 대한 상세페이지)


## ❗ Reference
- 이 프로젝트는 [**SPAO**](http://spao.com/) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무 수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제가 될 수 있습니다.

### 🙏 help   
- 프로젝트 상품 이미지 출처원 : [**MIDEOCK-미덕**](http://mideock.kr/) , [**SARNO-사르노**](http://sarno.co.kr/) *이미지 사용을 허가해주신 대표님들께 감사합니다.
- 해당 프로젝트의 이미지를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제가 될 수 있습니다.
