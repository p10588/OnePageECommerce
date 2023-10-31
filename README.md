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
![image](https://github.com/p10588/OnePageEcommerce/assets/12834223/4344502d-c8cd-434a-b5df-15b17853807b)

## 服務職責拆分
 - Order_Service
 <br/>
 
 - Auth_Service
 <br/>
 
 - Shop_Service
 <br/>
 
 - Product_Service
 <br/>
 
 - Email Service
 <br/>
 
 - Payment Service
 <br/>
 
 - Logistics Service
 <br/>
 
 - Inventory Service
 <br/>

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





