from fastapi import APIRouter
from domen.single_channel_query import SingleChannelQuery
from domen.multi_channel_query import MultiChannelQuery

router = APIRouter(
    prefix="/v1/api", tags=["v1"], responses={404: {"description": "Not found"}}
)

@router.post("/query/single_channel")
def get_single_queuing_theory_solution(average_time: float, intensity: float):

    single_channel_query = SingleChannelQuery()
    queuing_theory_solution_answer = single_channel_query.get_single_queuing_theory_solution(intensity, average_time)

    return {"sinle_channel_queuing_theory_solution": queuing_theory_solution_answer}


@router.post("/query/multichannel")
def get_multi_queuing_theory_solution(intensity: float, number_of_channels: int, average_time: float):
    print(intensity)
    multi_channel_query = MultiChannelQuery()
    queuing_theory_solution_answer = multi_channel_query.get_multi_queuing_theory_solution(intensity, number_of_channels, average_time)

    return {"multi_channel_queuing_theory_solution": queuing_theory_solution_answer}
