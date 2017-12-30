import argparse
import sys
import JenkinsConfiguration

from jenkinsapi.jenkins import Jenkins

# https://jenkinsapi.readthedocs.io/en/latest/
jenkins = Jenkins(JenkinsConfiguration.jenkinsurl)

def printNodeNames():
    jenkins = Jenkins(JenkinsConfiguration.jenkinsurl)
    node_names = jenkins.get_nodes()
    for name in node_names.keys():
        print(name)

def printOfflineNodes():
    jenkins = Jenkins(JenkinsConfiguration.jenkinsurl)
    node_names = jenkins.get_nodes()
    for item, value in node_names.iteritems():
        if (value.is_online()==False):
            print(item)

def printAllJobs():
    jenkins = Jenkins(JenkinsConfiguration.jenkinsurl)
    jobs = jenkins.get_jobs()
    for key,value in jobs:
        print (key)

def printInstalledPlugins():
    jenkins = Jenkins(JenkinsConfiguration.jenkinsurl,JenkinsConfiguration.username,JenkinsConfiguration.password)
    plugin_names = jenkins.get_plugins()
    for item in plugin_names.keys():
        print (item)

p = argparse.ArgumentParser()
subparsers = p.add_subparsers()

option1_parser = subparsers.add_parser('nodeNames')
option1_parser.set_defaults(func=printNodeNames)

option2_parser = subparsers.add_parser('offlineNodes')
option2_parser.set_defaults(func=printOfflineNodes)

option3_parser = subparsers.add_parser('allJobs')
option3_parser.set_defaults(func=printAllJobs)

option4_parser = subparsers.add_parser('plugins')
option4_parser.set_defaults(func=printInstalledPlugins)

args = p.parse_args()
args.func()

if __name__ == "__main__":
    option, params = sys.argv[0], sys.argv[1:]