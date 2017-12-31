import argparse
import sys
import JenkinsConfiguration

from jenkinsapi.jenkins import Jenkins


# https://jenkinsapi.readthedocs.io/en/latest/

def connectToServer():
    try:
        jenkins = Jenkins(JenkinsConfiguration.jenkinsurl, JenkinsConfiguration.username, JenkinsConfiguration.password)
    except:
        print("There was an error connecting to the Jenkins Server. Ensure the URL and credentials are correct")
    return jenkins


def printNodeNames():
    jenkins = connectToServer()
    node_names = jenkins.get_nodes()
    for name in node_names.keys():
        print(name)


def printOfflineNodes():
    jenkins = connectToServer()
    node_names = jenkins.get_nodes()
    for item, value in node_names.iteritems():
        if (value.is_online() == False):
            print(item)


def printAllJobs():
    jenkins = connectToServer()
    jobs = jenkins.get_jobs()
    for key, value in jobs:
        print(key)


def printInstalledPlugins():
    jenkins = connectToServer()
    plugin_names = sorted(jenkins.get_plugins().keys(), key=lambda x: x.lower())
    for item in plugin_names:
        print(item)


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
