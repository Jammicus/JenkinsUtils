import argparse
import os
import sys
import time

from jenkinsapi.custom_exceptions import JenkinsAPIException
from jenkinsapi.jenkins import Jenkins

scriptpath = "Credentials.py/../"
sys.path.append(os.path.abspath(scriptpath))

import Credentials

# https://jenkinsapi.readthedocs.io/en/latest/

def printAllNodeLabels():
    jenkins = connectToServer()
    listOfLabels = []
    node_names = getNodeNames()
    for node in node_names.keys():
        try:
            print("Getting labels for " + node)
            results = (jenkins.get_node(node).get_labels())
            listOfLabels.extend(results.split())
            # Prevent the API blocking requests
            time.sleep(3)
        except JenkinsAPIException:
            print(node + " does not have a config file, so its labels could not be found")
            # Prevent the API blocking requests
            time.sleep(3)
            continue
    print(set(listOfLabels))


def getNodeNames():
    jenkins = connectToServer()
    node_names = jenkins.get_nodes()
    return node_names


def printNodeNames():
    connectToServer()
    node_names = getNodeNames()
    for name in node_names.keys():
        print(name)


def printOfflineNodes():
    connectToServer()
    node_names = getNodeNames()
    for item, value in node_names.iteritems():
        if (value.is_online() == False):
            print(item)


def printAllJobs():
    jenkins = connectToServer()
    jobs = jenkins.get_jobs_list()
    print("\n".join(jobs))


def printInstalledPlugins():
    jenkins = connectToServer()
    plugins = jenkins.get_plugins().values()
    plugins.sort(key=lambda x: x.shortName.lower())
    for item in plugins:
        print(item.shortName)


def printEnabledPlugins():
    jenkins = connectToServer()
    plugins = jenkins.get_plugins().values()
    plugins.sort(key=lambda x: x.shortName.lower())
    for item in plugins:
        if item.enabled == True:
            print(item)


def printDisabledPlugins():
    jenkins = connectToServer()
    plugins = jenkins.get_plugins().values()
    plugins.sort(key=lambda x: x.shortName.lower())
    for item in plugins:
        if item.enabled == False:
            print(item)


def printInstalledPluginsVersions():
    jenkins = connectToServer()
    plugins = jenkins.get_plugins().values()
    plugins.sort(key=lambda x: x.shortName.lower())
    for item in plugins:
        print(item.shortName + " " + item.version)


def printInstalledPluginsURL():
    jenkins = connectToServer()
    plugins = jenkins.get_plugins().values()
    plugins.sort(key=lambda x: x.shortName.lower())
    for item in plugins:
        print(item.shortName + " " + item.url)


def printJenkinsVersion():
    jenkins = connectToServer()
    serverInformation = jenkins.get_jenkins_obj()
    print("Jenkins Version is " + serverInformation.version)


def printRunningJobs():
    jenkins = connectToServer()
    jobs = jenkins.get_jobs()
    for name, details in jobs:
        if (details.is_running()):
            print(name)


def printJobQueue():
    jenkins = connectToServer()
    jobs = jenkins.get_queue()
    for name in jobs():
        print(name)


def connectToServer():
    try:
        jenkins = Jenkins(Credentials.jenkinsurl, Credentials.username, Credentials.password)
    except:
        print("There was an error connecting to the Jenkins Server. Ensure the URL and credentials are correct")
        exit(1)
    return jenkins


def printJobQueueLength():
    jenkins = connectToServer()
    jobs = jenkins.get_queue()
    print(len(jobs))


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

option5_parser = subparsers.add_parser('enabledPlugins')
option5_parser.set_defaults(func=printEnabledPlugins)

option6_parser = subparsers.add_parser('disabledPlugins')
option6_parser.set_defaults(func=printDisabledPlugins)

option7_parser = subparsers.add_parser('pluginVersions')
option7_parser.set_defaults(func=printInstalledPluginsVersions)

option8_parser = subparsers.add_parser('pluginUrl')
option8_parser.set_defaults(func=printInstalledPluginsURL)

option9_parser = subparsers.add_parser('jenkinsVersion')
option9_parser.set_defaults(func=printJenkinsVersion)

option10_parser = subparsers.add_parser('possibleLabels')
option10_parser.set_defaults(func=printAllNodeLabels)

option11_parser = subparsers.add_parser('runningJobs')
option11_parser.set_defaults(func=printRunningJobs)

option12_parser = subparsers.add_parser('queue')
option12_parser.set_defaults(func=printRunningJobs)

option13_parser = subparsers.add_parser('queuelength')
option13_parser.set_defaults(func=printJobQueueLength)

args = p.parse_args()
args.func()

if __name__ == "__main__":
    option, params = sys.argv[0], sys.argv[1:]
