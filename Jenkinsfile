pipeline {
    agent { docker 'python:3.6.3' }
    stages {
        stage('build') {
            steps {
                sh 'sh JenkinsBuild.sh'
            }
        }
    }
}
