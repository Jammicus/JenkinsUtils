from jenkinsapi.jenkins import Jenkins
import JenkinsConfiguration
import itertools

# https://jenkinsapi.readthedocs.io/en/latest/
jenkins = Jenkins(JenkinsConfiguration.jenkinsurl)


def printNodeNames():
    node_names = jenkins.get_nodes()
    for name in node_names.keys():
        print(name)

def printOfflineNodes():
    node_names = jenkins.get_nodes()
    for item, value in node_names.iteritems():
        if (value.is_online()==False):
            print(item)

def printAllJobs():
    jobs = jenkins.get_jobs()
    for key,value in jobs:
        print (key)



if __name__ == "__main__":
    # printNodeNames()
    printAllJobs()