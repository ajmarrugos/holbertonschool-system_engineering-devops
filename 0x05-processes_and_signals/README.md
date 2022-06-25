## Bash: Processes & Signals

Useful project excersice to remember some commands used in bash to accomplish certain proccess tasks:

- Showing processes information
- Seeking procceses and killing them
- Infinite looping with waiting time intervals
- Hearing signals and printing them

This are the scripts implemented:

| File/Script                       | Use/Description                                                                   |
| --------------------------------- | --------------------------------------------------------------------------------- |
| 0-what-is-my-pid                  | Will show the current script's PID                                                |
| 1-list_your_processes             | Will show a list of current running processes as User format                      |
| 2-show_your_bash_pid              | Will show list af running processes named with 'bash' word                        |
| 3-show_your_bash_pid_made_easy    | Will displays PID and the name of running processes with 'bash'                   |
| 4-to_infinity_and_beyond          | Will print a message indefinitely and wait 2 secs on every iteration              |
| 5-dont_stop_me_now                | Will look for every running process that has 'beyond' word and kill it (kill)     |
| 6-stop_me_if_you_can              | Will look for every running process that has 'beyond' word and kill it (pkill)    |
| 7-highlander                      | Will print a message indefinitely and print another when hears a signal           |
| 8-beheaded_process                | Will kill a specific running process with a name of file 'highlander'             |