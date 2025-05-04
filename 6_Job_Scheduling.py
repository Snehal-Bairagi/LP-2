# Function to schedule jobs for maximum profit
def job_scheduling(jobs, n):
    # Sort jobs by descending order of profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [False] * (max_deadline + 1)  # Slots 1 to max_deadline
    job_sequence = [None] * (max_deadline + 1)
    total_profit = 0

    for job_id, deadline, profit in jobs:
        # Find a free slot from deadline to 1
        for t in range(min(deadline, max_deadline), 0, -1):
            if not slots[t]:
                slots[t] = True
                job_sequence[t] = job_id
                total_profit += profit
                break

    scheduled_jobs = [job for job in job_sequence if job]
    return scheduled_jobs, total_profit

# ---- Main program ----

n = int(input("Enter number of jobs: "))
jobs = []

print("Enter each job as: JobID Deadline Profit")
for _ in range(n):
    job_input = input().split()
    job_id = job_input[0]
    deadline = int(job_input[1])
    profit = int(job_input[2])
    jobs.append((job_id, deadline, profit))

scheduled_jobs, max_profit = job_scheduling(jobs, n)

print("\nScheduled Jobs:", ' -> '.join(scheduled_jobs))
print("Maximum Profit:", max_profit)
