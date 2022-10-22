
<h1 align="center">
  <img src="https://user-images.githubusercontent.com/52315048/197318654-db7e7801-3179-4e00-8097-67406dbe7c2e.svg" width="620px" alt="sutrace">
</h1>

## すっとトレース、Sutrace

![demo](https://user-images.githubusercontent.com/52315048/197320638-48a1fd3d-e6ff-46e5-a745-a79c87821999.gif)


## 製品概要
Sutraceは、GitHubで公開されているリポジトリを用いて、コミットごとに写経が出来る体験型の学習サイトです。参考にするプログラムを写して学習する、いわゆる「写経」のハードルを下げることを目的として開発しています。Sutraceを使って、コミットを追いながら写経すれば、見慣れたプログラムの新たな側面が見えてくるかもしれません。

### 背景(製品開発のきっかけ、課題等）

Sutraceの開発のきっかけは、新入生歓迎会でプログラミングを教えることの難しさを感じたことと、サークルだけでは得られないような、新たな開発手法やフレームワークへの興味です。

一方で、すでにそのような課題に対して確立された学習方法はありますが、私たちが大事にしたいのは「手を動かす」ということでした。学びにおいては、ロジックの理解だけではなく、自分の手元に再現するという行為を通じて、学ぶ対象についてより深い理解を得ることができます。

特に、環境構築などのプログラムを書く前段階の工程を意図的に回避し、既存のプログラムをなぞる「写経」というアプローチを取ることで、手を動かしながら、ストレスレスに、新たな分野へ挑戦することができます。

そこで、カジュアルに初心者でも経験者でも学ぶことができる「写経」を行うプラットフォームを提供することで、プログラムの書き方を学ぶことから、新たなフレームワークを学ぶことまで、様々なレベルに応じた学習ニーズを深く満たせるのではないかと考えました。

### 製品説明（具体的な製品の説明）
Sutraceを使うことで、GitHub上で公開されている好きなリポジトリを選び、コミットごとに合わせて「写経」し、学習することができます。自分の進捗は保存され、いつでも自分のペースで学習を進めることができます。写経する際には、後ろに薄く表示されている元のリポジトリのコードを見ながら学習を進めましょう。

### 特徴
#### Gitリポジトリのコミットに沿って学ぶことができる
それぞれのコミットで、実際のプログラムを通じて、自分の手を動かしながら学ぶことができます。また、対象としているリポジトリの開発者が、そのコミットに込めた意図や意思も確認し、学習の支えとすることができます。

#### 誘導とともにプログラムを書くことができる
利用者が初めて触れる言語やフレームワークでも、先達のプログラムを参考にしながら、その肌感や、特有の書き方に慣れ親しむことができます。また、言語化されない細かなテクニックや、関数の分割などのメタ的な部分も含めて学ぶことができるので、実際に自分でアウトプットする際の堅固な基礎を築くことができます。

### 解決できること
プログラムをなぞる「写経」という学習方法を通じて、教本よりも実践的で、実際の環境で行うよりもカジュアルにプログラミングの習得ができます。また、コミットの切り方や、実用上のテクニックなども学ぶことができます。

### 今後の展望

 今後の展望としては、まず通常機能の実装を予定しています。その後、実行環境の提供や、ユーザーページの提供など、通常の学習サイトのような機能追加を行いたいと考えています。

### 注力したこと（こだわり等）

開発のきっかけにより少ない手数で技術に習熟することもあり、少ない操作で写経が始められるように工夫しました。


## 開発技術

フロントエンドはNext.jsを使っています。またエディタ部分では、利用者に親しみ深いUIで利用のハードルを下げることを意図し、Visual Studio Codeでも用いられるMonaco Editorを採用しています。アカウント認証では、GitHubアカウントを利用することで、利用時の手間の軽減を目指しました。

バックエンドではFastAPIを用いて、ユーザーのリポジトリごとの進捗状況の管理などを行っています。フロントエンドサーバーにAPIのみを提供するため、他のPythonのフレームワークよりも簡潔にエンドポイントが設定でき、学習コストも低いFastAPIを採用しました。
