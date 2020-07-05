# Châteaubriand Serverside
## App
The app contains the logic of the server.<br/>
The app architecture uses MVC.
### Components
- Models : Application Model that is the interface between the server and the database.
- Views : Application Model에 쿼리 하여 Response Data를 만듭니다.
- Controllers : URI를 Mapping하고 Application Model에 쿼리 하여 Application Model를 바꿉니다.
- Exceptions : 에러 발생에 관하여 정의 합니다.
- Extensions : 외부 서비스에 대해 정의 합니다.
- Services : 서비스 로직에 대해 정의 합니다.
## Config
설정 사항을 정의합니다.
### Components
- AppConfig : App에 사용될 설정 사항을 정의 합니다.
- DBConfig : DB에 관한 설정 사항을 정의 합니다.
## Const
상수 값에 대해 정의 합니다.
## Test
테스트 코드를 작성 하는 곳 입니다. Python의 Unittest를 사용합니다.<br/>
테스트 대상은 DockerImage에 의해 생성된 컨테이너안의 서버 입니다.<br/>
테스트 하는 정보는 다음과 같습니다.
- Config : 설정 사항이 제대로 적용되었는지 테스트 합니다.
- Api : Api가 제 기능을 하는지 테스트 합니다.