from fastapi import APIRouter
from domain.single_channel_queue import SingleChannelQueue
from domain.multi_channel_queues import MultiChannelQueueWithRejection, MultiChannelQueueWithExpectation

router = APIRouter(
    prefix="/api/v1", tags=["v1"], responses={404: {"description": "Not found"}}
)

@router.post("/queue/single_channel")
def get_single_queuing_theory_solution(average_time: float, intensity: float):

    single_channel_queue = SingleChannelQueue()
    queuing_theory_solution_answer = single_channel_queue.get_single_queuing_theory_solution(intensity, average_time)

    return {"single_channel_queuing_theory_solution": queuing_theory_solution_answer}


@router.post("/queue/multi_channel_with_rejection")
def get_multi_queuing_theory_solution(intensity: float, number_of_channels: int, average_time: float):

    multi_channel_queue = MultiChannelQueueWithRejection()
    queuing_theory_solution_answer = multi_channel_queue.get_multi_queuing_theory_solution(intensity, number_of_channels, average_time)

    return {"multi_channel_queuing_theory_solution": queuing_theory_solution_answer}

@router.post("/queue/multi_channel_with_expectation")
def get_multi_queuing_theory_solution_with_expectation(requests_flow_rate:float, service_flow_rate:float, number_of_channels:int):

    multi_channel_queue = MultiChannelQueueWithExpectation()
    queuing_theory_solution_answer = multi_channel_queue.get_multi_queuing_theory_solution(requests_flow_rate, service_flow_rate, number_of_channels)

    return {"multi_channel_queuing_theory_solution": queuing_theory_solution_answer}
