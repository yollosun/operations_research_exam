<script lang="ts" setup>
import PButton from 'primevue/button';
import { solveSingleQueuingTheory } from '~~/services/single_queue_channel';
import { solveMultiQueuingTheoryWithRejection } from '~~/services/multiple_queue_channel_with_rejection';
import { solveMultiQueuingTheoryWithExpectation } from '~~/services/multiple_queue_channel_with_expectation';

definePageMeta({ title: 'Single', layout: 'main' })

const solve_queue_parameters = async () => {
    const result = await solveSingleQueuingTheory(45, 1.5)
    console.log(result)
}

const solve_queue_parameters2 = async () => {
    const result = await solveMultiQueuingTheoryWithRejection(45, 1.5, 6)
    console.log(result)
}

const solve_queue_parameters3 = async () => {
    const result = await solveMultiQueuingTheoryWithExpectation(4, 1.5, 6)
    console.log(result)
}

</script>

<template>
    <div>
        <PButton label="Создать" class="bg-[#060E28] b-[#060E28] m-t-5" @click="solve_queue_parameters" />
        <PButton label="Создать" class="bg-[#060E28] b-[#060E28] m-t-5" @click="solve_queue_parameters2" />
        <PButton label="Создать" class="bg-[#060E28] b-[#060E28] m-t-5" @click="solve_queue_parameters3" />
    </div>

</template>