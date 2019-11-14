import gym


if __name__ == "__main__":
    env = gym.make("CartPole-v0")
    # Record the environment - remove Force=True to prevent overwriting
    env = gym.wrappers.Monitor(env, "~/tmp/recording", force=True)

    total_reward = 0.0
    total_steps = 0.0
    obs = env.reset()

    while True:
        env.render(mode="human")                        # Display the cart
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)
        total_reward += reward
        total_steps += 1
        if done:
            break

    print(f"Episode done {total_steps} steps, total reward {total_reward:.2f} ")
    env.close()
    env.env.close()
