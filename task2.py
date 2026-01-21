from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    jobs = [PrintJob(**job) for job in print_jobs]
    printer = PrinterConstraints(**constraints)

    jobs.sort(key=lambda job: job.priority)

    print_order = []
    total_time = 0

    i = 0
    while i < len(jobs):
        current_group = []
        current_volume = 0
        group_time = 0

        while (
            i < len(jobs)
            and len(current_group) < printer.max_items
            and current_volume + jobs[i].volume <= printer.max_volume
        ):
            current_group.append(jobs[i])
            current_volume += jobs[i].volume
            group_time = max(group_time, jobs[i].print_time)
            i += 1

        if not current_group:
            job = jobs[i]
            print_order.append(job.id)
            total_time += job.print_time
            i += 1
        else:
            for job in current_group:
                print_order.append(job.id)
            total_time += group_time

    return {
        "print_order": print_order,
        "total_time": total_time
    }
