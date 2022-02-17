import pytest

from httprunner import (HttpRunner, Config, Step, RunRequest, Parameters, RunTestCase)


class TestCaseLogin(HttpRunner):
    @pytest.mark.parametrize('param', Parameters({'number': [1, 2], 'token_length': [32]}))
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("login")
            .variables(
            **{"username": "${ENV(USERNAME)}",
               "password": "${ENV(PASSWORD)}"
               }
        )
            .base_url("${ENV(HOSTURL)}")
            .verify(False)
        # .export(*["param"])
    )
    teststeps = [
        Step(
            RunRequest('login')
                .with_variables(**{'status_code': 201, 'status': 1})
                .post('/client/user/auth')
                .with_headers(**{"Content-Type": "application/json"})
                .with_json({"scenario": "client", "company_id": 5940, "user_name": "$username", "password": "$password",
                            "device_type": "$number", "device": ""})
                .extract()
                .with_jmespath("body.data.token", "token")
                .validate()
                .assert_equal('status_code', '$status_code', '断言失败')
                .assert_equal('body.status', '$status', '断言失败')
                .assert_length_equal('body.data.token', '$token_length', '断言失败')
        )
    ]


if __name__ == "__main__":
    TestCaseLogin().test_start()
