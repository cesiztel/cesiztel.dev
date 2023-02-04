from distutils.core import run_setup
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_apigateway as apigw
)
from constructs import Construct

class ServerlessTodoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Add task lambda function declaration
        add_task_function = _lambda.Function(
            self,
            "AddTaskFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset("tasks/add"),
            handler="add_task.handler"
        )

        todo_policy = iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=['*'],
            actions=['events:PutEvents']
        )

        add_task_function.add_to_role_policy(todo_policy)

        # Complete task lambda function declaration
        complete_task_function = _lambda.Function(
            self,
            "CompleteTaskFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset("tasks/complete"),
            handler="complete_task.handler"
        )

        complete_task_function.add_to_role_policy(todo_policy)

        # Delete task lambda function declaration
        delete_task_function = _lambda.Function(
            self,
            "DeleteTaskFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset("tasks/delete"),
            handler="delete_task.handler"
        )

        delete_task_function.add_to_role_policy(todo_policy)

        # Get all tasks lambda function declaration
        get_all_tasks_function = _lambda.Function(
            self,
            "GetAllTasksFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset("tasks/all"),
            handler="get_all_tasks.handler"
        )

        get_all_tasks_function.add_to_role_policy(todo_policy)

        # Get a single task lambda function declaration
        get_task_function = _lambda.Function(
            self,
            "GetTaskFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset("tasks/get"),
            handler="get_task.handler"
        )

        get_task_function.add_to_role_policy(todo_policy)

        # Update task lambda function declaration
        update_task_function = _lambda.Function(
            self,
            "UpdateTaskFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset("tasks/update"),
            handler="update_task.handler"
        )

        update_task_function.add_to_role_policy(todo_policy)

        """
        api = apigw.RestApi(
            self,
            'Serverless-ToDo-API',
            rest_api_name='serverless-todo-api'
        )

        add_todo = api.root.add_resource('tasks')
        add_todo_integration=apigw.LambdaIntegration(add_todo_function)
        add_todo.add_method(
            'POST',
            integration=add_todo_integration
        )

        # Define deployment and stage depending on environment
        dev_deployment = apigw.Deployment(
            self,
            id='dev_deveployment',
            api=api
        )

        apigw.Stage(
            self,
            id='stage_dev',
            deployment=dev_deployment,
            stage_name='dev'
        )
        """

