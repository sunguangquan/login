# Git



### 什么是版本控制？

什么是“版本控制”？我为什么要关心它呢？ 版本控制是一种记录一个或若干文件内容变化，以便将来查阅特定版本修订情况的系统。





### Git的状态：

现在请注意，如果你希望后面的学习更顺利，请记住下面这些关于 Git 的概念。 Git 有三种状态，你的文件可能处于其中之一： **已提交（committed）**、**已修改（modified）** 和 **已暂存（staged）**。

* 已修改表示修改了文件，但还没保存到数据库中。
* 已暂存表示对一个已修改文件的当前版本做了标记，使之包含在下次提交的快照中。
* 已提交表示数据已经安全地保存在本地数据库中



### 基本的Git工作流程

1. 在工作区中修改文件。
2. 将你想要下次提交的更改选择性地暂存，这样只会将更改的部分添加到暂存区。
3. 提交更新，找到暂存区的文件，将快照永久性存储到 Git 目录





### Git全局配置

```Git
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com" #使用git bash 创建sshkey
$ eval $(ssh-agent -s) #在git 系统中使用key
$ clip < ~/.ssh/id_rsa.pub  #复值git的key
```

```console
$ git config --global user.name "Your name"  #配置姓名
$ git config --global user.email 'Your Email'  #配置邮箱
git config --list  #查看配置
```

### Git远程仓库

```git
git remote add <name> <url> #添加远程仓库
git push <name> <branch name> #推送到远程仓库
git pull <name> <branch name> #获取远程仓库
git fetch <name>  #获取远程仓库文件
```





### Git暂存文件

```git 
git add "filename"
git add * #添加全部文件
```

### Git提交
```git
git commit -m '描述信息'
```



### Git取消暂存

```git
git reset HEAD <filename>
git checkout --<fielname> 
```



### Git分支

```git
git branch <name> #创建分支
git checkout <name>  #切换分支
git checkout -b <name> #创建并切换分支
git branch -d <name> #删除分支
git merge name <name> #合并分支
#合并冲突需要手动修改文件，然后提交文件。最后完成合并
```

