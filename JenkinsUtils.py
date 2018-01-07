import argparse
import sys
import time

from jenkinsapi.custom_exceptions import JenkinsAPIException

import JenkinsConfiguration

from jenkinsapi.jenkins import Jenkins


# https://jenkinsapi.readthedocs.io/en/latest/

def connectToServer():
    try:
        jenkins = Jenkins(JenkinsConfiguration.jenkinsurl, JenkinsConfiguration.username, JenkinsConfiguration.password)
    except:
        print("There was an error connecting to the Jenkins Server. Ensure the URL and credentials are correct")
        exit(1)
    return jenkins


def printAllNodeLabels():
    jenkins = connectToServer()
    listOfLabels = []
    node_names = jenkins.get_nodes()
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

option10_parser = subparsers.add_parser('runningJobs')
option10_parser.set_defaults(func=printRunningJobs)


args = p.parse_args()
args.func()

if __name__ == "__main__":
    option, params = sys.argv[0], sys.argv[1:]
