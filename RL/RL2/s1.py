import gym;

env = gym.make("Taxi-v2");
state = env.reset();
env.render();

cnt = 1;
reward = 0;
while reward != 20:
	action = env.action_space.sample();
	state, reward,done,info = env.step(action);
#	env.render();
	cnt = cnt + 1;
print("Needed " + str(cnt) + " moves to reach the final state");