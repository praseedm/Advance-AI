import gym;
import numpy as np;

Q = np.zeros([500,6]);
gamma = .801;

env = gym.make("Taxi-v2");


for episode in range(1,1000) :

	state = env.reset();
#	env.render();


	cnt = 1;
	reward = 0;
	while reward != 20:
		action = np.argmax(Q[state]);
#env.action_space.sample();
		state2, reward,done,info = env.step(action);
		Q[state,action] = reward + gamma * np.max(Q[state2]);
		state = state2;
#	env.render();
		cnt = cnt + 1;
	if episode % 50 == 0:
		print("Needed " + str(cnt) + " moves to reach the final state during episode " + str(episode));