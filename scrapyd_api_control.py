"""
ipython
>>> from scrapyd_api_control import Scrapyd_Control
>>> s = Scrapyd_Control()
>>> s.start
此程序只能针对一个项目控制（多个）爬虫，如果有另一个项目，需再另运行此程序
"""

from scrapyd_api import ScrapydAPI


class Scrapyd_Control():

    scrapyd_url = input('请输入scrapyd地址： ')
    project = input('请输入项目名称： ')
    scrapyd = ScrapydAPI(scrapyd_url)

    # 启动爬虫
    @property
    def start(self):
        spider = input('请输入爬虫名称： ')
        return {
            'project': self.project,
            'spider': spider,
            'jobid': self.scrapyd.schedule(self.project, spider)
            }

    # 取消爬虫
    @property
    def cancel(self):
        jobid = input('请粘贴要取消的爬虫jobid： ')
        return self.scrapyd.cancel(self.project, jobid)

    # 查看项目
    @property
    def listprojects(self):
        return self.scrapyd.list_projects()

    # 查看爬虫
    @property
    def listspiders(self):
        return self.scrapyd.list_spiders(self.project)

    # 列出所有jobs
    @property
    def listjobs(self):
        return self.scrapyd.list_jobs(self.project)

    # 查看job状态
    @property
    def jobstatus(self):
        jobid = input('请粘贴要查看的jobid: ')
        return self.scrapyd.job_status(self.project, jobid)

    # 查看版本
    @property
    def listversions(self):
        return self.scrapyd.list_versions(self.project)

    # 删除版本
    @property
    def delversion(self):
        version_name = input('请粘贴要删除的版本： ')
        return self.scrapyd.delete_version(self.project, version_name)

    # 删除项目
    @property
    def delproject(self):
        self.scrapyd.delete_project(self.project)
        
        
