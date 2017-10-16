pipeline {
    agent { docker 'python:2.7.10' }
    stages {
        stage('build') {
            steps {
                sh 'sh JenkinsBuild.sh'
            }
        }
    }
}
