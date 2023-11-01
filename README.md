# 一頁式商城後台 OnePageEcommerce Backend
One-page e-commerce backend in Python
 <br/> 
 <br/>  
## 動機目的
 - 運用TDD與DDD進行一頁式電商後台開發  
最終目標是開發一個的分散式微服務  
具擴展性、高適應性、可漸進式變更、安全（架構特性持續優化)  
並紮實學習各種後端技術與架構  
 <br/> 
 
## 技術關鍵字
 - 領域驅動開發、領域建模，資料模型、Aggregate  
 - 測試驅動開發、單元測試、整合測試、端到端測試、pytest、postman  
 - 服務式架構、無狀態服務、高擴展性、WebApi、Flask、依賴反轉  
 - 關連式資料庫、抽象資料層、PostgreSQL、Repository模式，Unit of Work模式  
 <br/>

## 技術內容
 - 語言：Python 3.11
 - 隔離環境：python virtualenv  
 - 框架：python flask  
 - 資料庫：postgreSQL + python psycogy2  
 - 測試框架：pytest + postman  
 <br/>

## 架構圖
![image](https://github.com/p10588/OnePageEcommerce/assets/12834223/db0c794a-7aa9-4757-aa85-e5ad4456489b)

## 資料關聯
![image](https://github.com/p10588/OnePageEcommerce/assets/12834223/397814de-d6f6-4e0f-98db-45dd6da122e8)

## 服務職責拆分
   
 - **Cart_Service：** 
   
   負責購物車業務領域並整合Cookie服務

   > - add to cart
   > - remove from cart
   > - get cart 
   > - clear cart

   - 待優化
     - [ ] 將CookieSevice用Repo抽象層隔離，跟CartService解耦合

- **Product_Service (WIP)**
  
  商品相關，主要提供商城中商品資料與商品細節的呈現
  
  > - get all products
  > - add product
  > - remove product
  > - update product
  > - import product list
  
  - 待優化
     - [ ] 將資料庫操作原子化

 - **Order_Service：**  

   整合訂單領域邏輯，用工廠模式管理訂單流程(order_flow)，整合物流、金流、倉儲服務  
   通知與更新狀態
   
   > - get user order
   > - place order
   > - update order status (WIP)
   > - update payment status (WIP)
   > - update shipping status (WIP)

 - **Auth_Service (WIP)**
   
   用戶與認證相關業務，包含用戶權限管理，用工廠模式整合OAuth2.0，以抽象快速擴充
   
   > - login
   > - signin
   > - logout
   > - update user permission
   > - update user data
   > - get api key

- **Inventory Service (WIP)**
  
  以服務層跟訂單服務串接，以抽象層來分離跟庫存系統的溝通，目標是不管是跟外部的倉儲  
  系統或自建的倉儲系統都可以透過Rest交換訊息
 
 - **Payment Service (WIP)**
   
   以服務層跟訂單服務串接，以抽象工廠來讓不同第三方支付方式可以擴充，以Rest的方式  
   將資料打到第三方進行付款處理，再由訂單服務以Rest接受callback結果

 - **Logistics Service (WIP)**
   
   以服務層跟訂單服務串接，以抽象工廠來讓物流方式得以擴充或替換，以Rest的方式將資料  
   打到第三方物流，由物流中心透過Rest將物流狀態回報至訂單服務

 - **Shop_Service (規劃中)**
   
   商城外觀相關服務

 - **Email Service (規劃中)**
   
   Email服務串接第三方Email服務，讓各服務可以寄出Eamil通知

## 技術架構

### Api層：
 - flask框架，搭配blueprint解耦Api層與服務層，進行Api版本管理，並提供統一部署與分散部署的彈性
 
 - api例外處理與追蹤
 
 - 待執行項目
      - [ ] 解耦資料庫設定
      - [ ] 完整的例外處理功能
      - [ ] Api存取權限管理，整合api裝飾器，檢查用戶權限
      - [ ] 整合日誌與監控
 <br/>

### 服務層：
 - 資料格式驗證
      
 - 整合領域跟資料層的組件
    
 <br/>
 
### 領域層：
- 建立領域模型與資料模型
 
- 處理領域相關的商務邏輯
      
- 處理領域限制
      
- 待執行項目
  - [ ] 釐清部分領域跟服務層模糊的職責
 <br/>
 
### 資料層
- Repository模式，搭配依賴反轉，建立資料抽象層，並提高資料庫種類的適應性，也提升可測試性

- Uow模式，原子化CUD操作，維持一致性
 <br/>
 
### 測試
- 領域單元測試

- Repo單元測試

- 用Postman進行E2E測試

- 待執行項目
  - [ ] 自動化測試 當flask 執行時可以自動E2E Test、 Unit Test

### 部署
 - 每個Flask皆可以獨立部署，目前編譯器部署與Terminal部署，分別使用不同的PORT
   
 - 待執行項目
   - [ ] Docker化服務





