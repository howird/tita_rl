from configs import TitaRoughCfg, TitaRoughCfgPPO


class TitaFlatCfg(TitaRoughCfg):
    class env(TitaRoughCfg.env):
        num_envs = 8192
        num_propriceptive_obs = 27 + 6 + 2
        num_privileged_obs = 152
        num_actions = 8
        env_spacing = 100.0
        send_timeouts = True
        episode_length_s = 20

    class terrain(TitaRoughCfg.terrain):
        mesh_type = 'plane'
        horizontal_scale = 0.1
        vertical_scale = 0.005
        border_size = 50
        curriculum = False
        static_friction = 0.4
        dynamic_friction = 0.6
        restitution = 0.8
        measure_heights_actor = False
        measure_heights_critic = False

    class commands(TitaRoughCfg.commands):
        curriculum = False
        max_curriculum = 1.
        num_commands = 3
        resampling_time = 10.
        heading_command = False

        class ranges:
            lin_vel_x = [-1.0, 1.0]
            lin_vel_y = [-0.0, 0.0]
            ang_vel_yaw = [-1, 1]
            heading = [-3.14, 3.14]

    class init_state(TitaRoughCfg.init_state):
        pos = [0.0, 0.0, 0.34]
        rot = [0.0, 0.0, 0.0, 1.0]
        lin_vel = [0.0, 0.0, 0.0]
        ang_vel = [0.0, 0.0, 0.0]
        pos_noise = 0.1
        rot_noise = 0.1
        default_joint_angles = {
            "joint_left_leg_1": 0.0,
            "joint_right_leg_1": 0.0,
            "joint_left_leg_2": 1.3,
            "joint_right_leg_2": 1.3,
            "joint_left_leg_3": -2.6,
            "joint_right_leg_3": -2.6,
            "joint_left_leg_4": 0.0,
            "joint_right_leg_4": 0.0,
            "joint_left_leg_4_1": 0.0,
            "joint_right_leg_4_1": 0.0,
            "joint_left_leg_4_2": 0.0,
            "joint_right_leg_4_2": 0.0,
            "joint_left_leg_4_3": 0.0,
            "joint_right_leg_4_3": 0.0,
            "joint_left_leg_4_bar": 0.0,
            "joint_right_leg_4_bar": 0.0,
        }

    class control(TitaRoughCfg.control):
        control_type = "P_AND_V"
        stiffness = {
            "joint_left_leg_1": 30,
            "joint_left_leg_2": 30,
            "joint_left_leg_3": 30,
            "joint_right_leg_1": 30,
            "joint_right_leg_2": 30,
            "joint_right_leg_3": 30,
            "joint_left_leg_4": 0.0,
            "joint_right_leg_4": 0.0,
            "joint_left_leg_4_1": 0.0,
            "joint_right_leg_4_1": 0.0,
            "joint_left_leg_4_2": 0.0,
            "joint_right_leg_4_2": 0.0,
            "joint_left_leg_4_3": 0.0,
            "joint_right_leg_4_3": 0.0,
            "joint_left_leg_4_bar": 30,
            "joint_right_leg_4_bar": 30,
        }
        damping = {
            "joint_left_leg_1": 0.5,
            "joint_left_leg_2": 0.5,
            "joint_left_leg_3": 0.5,
            "joint_right_leg_1": 0.5,
            "joint_right_leg_2": 0.5,
            "joint_right_leg_3": 0.5,
            "joint_left_leg_4": 0.5,
            "joint_right_leg_4": 0.5,
            "joint_left_leg_4_1": 0.5,
            "joint_right_leg_4_1": 0.5,
            "joint_left_leg_4_2": 0.5,
            "joint_right_leg_4_2": 0.5,
            "joint_left_leg_4_3": 0.5,
            "joint_right_leg_4_3": 0.5,
            "joint_left_leg_4_bar": 0.5,
            "joint_right_leg_4_bar": 0.5,
        }
        action_scale = 0.5
        action_scale_pos = 0.25
        action_scale_vel = 8
        decimation = 4

    class asset(TitaRoughCfg.asset):
        file = '{ROOT_DIR}/resources/tita/urdf/tita_description.urdf'
        name = 'tita'
        foot_name = '_leg_4'
        terminate_after_contacts_on = ["base_link", "_leg_3"]
        penalize_contacts_on = ["base_link", "_leg_3"]
        disable_gravity = False
        collapse_fixed_joints = True
        fix_base_link = False
        default_dof_drive_mode = 3
        self_collisions = 0
        replace_cylinder_with_capsule = True
        flip_visual_attachments = False
        density = 0.001
        angular_damping = 0.
        linear_damping = 0.
        max_angular_velocity = 1000.
        max_linear_velocity = 1000.
        armature = 0.
        thickness = 0.01

    class domain_rand(TitaRoughCfg.domain_rand):
        randomize_friction = True
        friction_range = [0.0, 1.6]
        randomize_base_mass = True
        added_mass_range = [-1., 2.]
        randomize_base_com = True
        rand_com_vec = [0.03, 0.02, 0.03]
        push_robots = True
        push_interval_s = 7
        max_push_vel_xy = 1.

    class rewards(TitaRoughCfg.rewards):
        class scales:
            action_rate = -0.01
            ang_vel_xy = -0.00
            base_height = -20.0
            collision = -10.0
            dof_acc = -2.5e-07
            dof_pos_limits = -2.0
            dof_vel = -0.0
            feet_air_time = 0.0
            feet_contact_forces = -0.0
            feet_stumble = -0.0
            lin_vel_z = -0.0
            no_fly = 1.0
            orientation = -5.0
            stand_still = -1.0
            termination = -0.0
            torque_limits = -0.1
            torques = -2.5e-05
            tracking_ang_vel = 5
            tracking_lin_vel = 10.0
            unbalance_feet_air_time = -0.0
            unbalance_feet_height = -0.0
            feet_distance = -100
            survival = 100
            wheel_adjustment = 1.0
            inclination = 0.0

        base_height_target = 0.4
        soft_dof_pos_limit = 0.95
        soft_dof_vel_limit = 0.9
        min_feet_distance = 0.57
        max_feet_distance = 0.60
        soft_torque_limit = 0.8
        max_contact_force = 200.
        only_positive_rewards = False
        min_feet_distance = 0.1
        min_feet_air_time = 0.25
        max_feet_air_time = 0.65
        tracking_sigma = 0.25
        nominal_foot_position_tracking_sigma = 0.005
        nominal_foot_position_tracking_sigma_wrt_v = 0.5
        leg_symmetry_tracking_sigma = 0.001

    class normalization(TitaRoughCfg.normalization):
        class obs_scales:
            lin_vel = 2.0
            ang_vel = 0.25
            dof_pos = 1.0
            dof_vel = 0.05
            height_measurements = 5.0

        clip_observations = 100.
        clip_actions = 100.

    class noise(TitaRoughCfg.noise):
        add_noise = True
        noise_level = 1.0

        class noise_scales:
            dof_pos = 0.01
            dof_vel = 1.5
            lin_vel = 0.1
            ang_vel = 0.2
            gravity = 0.05
            height_measurements = 0.1

    class viewer(TitaRoughCfg.viewer):
        ref_env = 0
        pos = [10, 0, 6]
        lookat = [11., 5, 3.]

    class sim(TitaRoughCfg.sim):
        dt = 0.005
        substeps = 1
        gravity = [0., 0., -9.81]
        up_axis = 1

        class physx:
            num_threads = 10
            solver_type = 1
            num_position_iterations = 4
            num_velocity_iterations = 0
            contact_offset = 0.01
            rest_offset = 0.0
            bounce_threshold_velocity = 0.5
            max_depenetration_velocity = 1.0
            max_gpu_contact_pairs = 2 ** 23
            default_buffer_size_multiplier = 5
            contact_collection = 2

class TitaFlatCfgPPO(TitaRoughCfgPPO):
    class policy(TitaRoughCfgPPO.policy):
        actor_hidden_dims = [256, 128, 64]
        critic_hidden_dims = [256, 128, 64]
        init_noise_std = 1.0

    class runner(TitaRoughCfgPPO.runner):
        experiment_name = 'tita_flat_14dof'
        max_iterations = 10000
