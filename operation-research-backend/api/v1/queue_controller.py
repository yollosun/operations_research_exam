from fastapi import APIRouter
from domen.single_channel_queue import SingleChannelQueue
from domen.multi_channel_queue import MultiChannelQueue

router = APIRouter(
    prefix="/api/v1", tags=["v1"], responses={404: {"description": "Not found"}}
)

@router.post("/queue/single_channel")
def get_single_queuing_theory_solution(average_time: float, intensity: float):

    single_channel_queue = SingleChannelQueue()
    queuing_theory_solution_answer = single_channel_queue.get_single_queuing_theory_solution(intensity, average_time)

    return {"sinle_channel_queuing_theory_solution": queuing_theory_solution_answer}


@router.post("/queue/multichannel")
def get_multi_queuing_theory_solution(intensity: float, number_of_channels: int, average_time: float):

    multi_channel_queue = MultiChannelQueue()
    queuing_theory_solution_answer = multi_channel_queue.get_multi_queuing_theory_solution(intensity, number_of_channels, average_time)

    return {"multi_channel_queuing_theory_solution": queuing_theory_solution_answer}
