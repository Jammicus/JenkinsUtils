from jenkinsapi.jenkins import Jenkins
import JenkinsConfiguration

# https://jenkinsapi.readthedocs.io/en/latest/
jenkins = Jenkins(JenkinsConfiguration.jenkinsurl)


def printNodeNames():
    node_names = jenkins.get_nodes()
    for name in node_names.keys():
        print (name)

if __name__ == "__main__":
    printNodeNames()