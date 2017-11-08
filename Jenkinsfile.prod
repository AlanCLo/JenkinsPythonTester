pipeline {
	agent none
		stages {
			stage('build') {
				agent { 
					docker {
						image 'python:2.7.10'
						args '-u root'
					}
				}
				steps {
					sh 'pip install -r requirements.txt'
					sh 'python manage.py migrate'
					sh 'python manage.py loaddata blahapp'
					sh 'coverage run manage.py test blahapp -v 2'
					sh 'coverage html'
					archive 'htmlcov/*'
				}
		}
		stage('build-container') {
			agent { 
				dockerfile {
					additionalBuildArgs '-t alan/blahapp'
				}
			}
			steps {
				sh 'coverage run manage.py test blahapp -v 2'
			}
		}
		stage('deploy') {
			when {
				expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
			}
			agent any
			steps {
				sh 'docker stop blahappdeployed || true && docker rm blahappdeployed || true'
				sh 'docker run -d -it -p 33000:8000 -e ALLOWED_HOST="`hostname -I`" --name=blahappdeployed alan/blahapp'
				sh 'docker cp $BLAHAPP_PROD_SETTINGS blahappdeployed:/usr/src/blahapp/tester/local_settings.py'
				sh 'docker stop blahappdeployed && docker start blahappdeployed'
			}
		}
	}
}





