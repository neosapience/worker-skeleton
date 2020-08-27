# worker skeleton

## developer

### default tests
1. replace task_custom -> {{your task}}
1. replace neosapience/appname-worker -> {{your image name as quay.io/neos/... }}
1. build base docker image
    ```bash
    $ make build-base
    ```

1. build image
    ```bash
    $ make build
    ```

1. test (celery eager = `TRUE` mode)
    ```
    & make test && make logs
    ```

1. test (celery redis queue mode)
    ```
    & make test-queue && make logs
    ```
