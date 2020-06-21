"""
初始化一个Git仓库
git init


添加文件到Git仓库，分两步：
第一步，使用命令,可多次添加文件
git add < file >
第二步，使用命令
git commit - m “log”


查看本地库状态
git status


比较库文件差异
git diff


查看提交历史（含commit_id，显示HEAD的版本是当前版本） Git
log


版本回退(回退到某个commit_id)
git reset –hard < commit_id >


版本回退(回退到当前版本上一个版本)
git reset –hard HEAD ^


对工作区的文件更改进行回退
git checkout - - < file >


将工作区的文件添加到暂存区这一步撤销
git reset HEAD < file >


分支
查看分支
git branch


创建分支
git branch < name >


切换分支
git checkout < name >


创建并切换分支
git checkout - b < name >


合并某分支到当前分支
git merge < name >


删除分支
git branch - d < name >
"""
