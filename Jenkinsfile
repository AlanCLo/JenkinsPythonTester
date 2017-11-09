#!groovy

node {
/*
	stage ('Build') {
		checkout scm
		docker.build('alan/blahapp')
	}
	stage ('Test') {
		docker.image('alan/blahapp').inside('-u root') {
			stage ('Setup tests') {
				sh 'pwd'
				sh 'python --version'
				sh 'python manage.py migrate'
				sh 'python manage.py loaddata blahapp'
			}
			stage ('Run tests') {
				sh 'coverage run manage.py test blahapp -v 2'
				sh 'coverage html'
			}
			stage ('Archive results') {
				archive (includes: 'htmlcov/*')
			}
		}
	}
*/
	if (BRANCH_NAME == "master") {
		stage ('QA') {
			undeploy(BLAHAPP_QA_SETTINGS)
			deploy(BLAHAPP_QA_SETTINGS)
		}

//sh 'echo "$BLAHAPP_PROD_SETTINGS"'
		//sh 'echo "${BRANCH_NAME}"'
		
	}
}

def deploy(settings) {
	sh "docker run -d -it -p `cat $settings/PORT`:8000 -e ALLOWED_HOST=\"`hostname -I`\" --name=`cat $settings/NAME` alan/blahapp"
	sh "docker cp $settings/local_settings.py `cat $settings/NAME`:/usr/src/blahapp/tester/local_settings.py"
	sh "docker exec `cat $settings/NAME` touch /usr/src/blahapp/tester/settings.py"
}

def undeploy(settings) {
	sh "docker stop `cat $settings/NAME` || true"
	sh "docker rm `cat $settings/NAME` || true"
}
