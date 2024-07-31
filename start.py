import asyncio

from prefect.client.orchestration import get_client
from prefect.client.schemas.filters import FlowFilter
from prefect.client.schemas.filters import FlowFilterName


async def main():
    async with get_client() as client:
        deployment = (await client.read_deployments(flow_filter=FlowFilter(name=FlowFilterName(any_=["my-flow"]))))[0]

        for i in range(0, 1):
            result = await client.create_flow_run_from_deployment(deployment.id, parameters={"i": i})
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
