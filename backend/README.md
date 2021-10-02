# APIエンドポイント(バックエンドApis)
## jobs（tags）
### jobs/create-job
　　POSTメソッド：DBに新しいジョブを書き込みます。
### jobs/get/{id}
　　GETメソッド：DBから特定IDのジョブ情報を取得します。
### jobs/all
　　GETメソッド：DBからすべてのジョブ情報を取得します。
### jobs/update/{id}
　　PUTメソッド：IDと更新するジョブ情報を指定し、DBを更新します。
### jobs/delete/{id}
　　DELETEメソッド：DBから特定IDのジョブを取り出し、ジョブ情報が存在すれば、DBからも削除します。

## users（tags）
### users/create-usere
　　新しいユーザをDBに作成します。

## login（tag）
### login/token
　　POSTメソッド：アクセストークンであるJWT TokenとToken typeを辞書型で返します。


# APIエンドポイント(フロントWebApp)
## homepage（tags）
### /
　　GETメソッド：ジョブリストを取得し、jobs/homepage.htmlで表示します。
### /detail/{id}
　　GETメソッド：ジョブIDに対応したジョブの詳細を取得し、jobs/detail.htmlに表示します。
### /post-a-job/
　　GETメソッド：追加するジョブの情報を入力するため、jobs/create_job.htmlで表示します。
　　POSTメソッド：requestからform dataを取得し、DBに新しいジョブを書き込みます。その後、/detail/{id}にリダイレクトします。
### /delete-job/
　　GETメソッド：各ジョブの横にdeleteボタンを付加したジョブ一覧を表示します。

### /search/
　　検索窓(id="query")の値を取得し、general_pages/homepage.htmlを表示します。

## users（tags）
### /register/
　　GETメソッド：signupページ表示のため、/users/register.htmlを表示します。
　　POSTメソッド：requestからform dataを取得し、新しいユーザを作成します。その後、/にリダイレクトします。

## auth（tags）
### /login/
　　GETメソッド：ログイン画面表示のため、auth/login.htmlを表示します。
　　POSTメソッド：requestからform dataを取得し、auth/login.htmlにform dataをわたします。その後、ログイン用アクセストークンを取得し、responseを返します。


# フォルダ構成
backend 
├ apis 
│ ├ version1 
│ │ ├ route_jobs.py 
│ │ ├ route_login.py 
│ │ └ route_users.py 
│ ├ base.py 
│ └ utils.py 
├ core 
│ ├ config.py 
│ ├ hashing.py 
│ └ security.py 
├ db 
│ ├ models 
│ │ ├ jobs.py 
│ │ └ users.py 
│ ├ repository 
│ │ ├ jobs.py 
│ │ ├ login.py 
│ │ └ users.py 
│ ├ base.py 
│ ├ base_class.py 
│ └ session.py 
├ htmlcov 
├ schemas 
│ ├ jobs.py 
│ └ users.py 
├ static 
│ ├ images 
│ │ └ logo.png 
│ └ js 
│    └ autocomplete.js 
├ templates 
│ ├ auth 
│ │ └ login.html 
│ ├ components 
│ │ ├ alerts.html 
│ │ ├ cards.html 
│ │ └ navbar.html 
│ ├ general_pages 
│ │ └ homepage.html 
│ ├ jobs 
│ │ ├ create_job.html 
│ │ ├ detail.html 
│ │ ├ homepage.html 
│ │ └ show_jobs_to_delete.html 
│ ├ shared 
│ │ ├ base.html 
│ └ users 
│    └ register.html 
├ tests 
│ ├ db 
│ │ └ test_jobs_repo.py 
│ ├ test_routes 
│ │ ├ test_jobs.py 
│ │ └ test_users.py 
│ ├ utils 
│ │ └ users.py 
│ └ conftest.py 
├ webapps 
│ ├ auth 
│ │ ├ forms.py 
│ │ └ route_login.py 
│ ├ jobs 
│ │ ├ forms.py 
│ │ └ route_jobs.py 
│ ├ users 
│ │ ├ forms.py 
│ │ └ route_users.py 
│ └ base.py 
├ .coverage 
├ .coveragerc 
├ .env 
├ main.py 
├ README.md 
├ requirements.txt 
├ sql_app.db 
└ test_db.db 
