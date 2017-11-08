#!groovy

node {
	stage ('Build') {
		checkout scm
		docker.build('alan/blahapp')
	}
	stage ('Test') {
		docker.image('alan/blahapp').inside {
			sh 'python manage.py migrate'
			sh 'python manage.py loaddata blahapp'
			sh 'coverage run manage.py test blahapp -v 2'
			sh 'coverage html'
		}
	}
}


