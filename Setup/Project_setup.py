import os
import subprocess
import sys


def check_python_version():
    
    print(f"\n|| System Python version: {sys.version}")


def is_windows():
    
    return os.name == 'nt'


def env_exists(env_path):
    
    return os.path.exists(env_path)


def notebook_setup():
    
    print(f"\n|| Set the environment \"Python\ds-challenge\" as the kernel for Jupyter Notebook")
    print("|| Use the folder \"Python\" from this repository")


def create_env(env_name='ds-challenge', build_dir='Build', python_dir='Python'):
    
    print("|| Creating virtual environment...")
    
    python_cmd = 'python' if is_windows() else 'python3'
    env_path = os.path.join(python_dir, env_name)
    requirements_file = os.path.join(build_dir, 'requirements.txt')
    
    if env_exists(env_path):
        
        print(f"|| Environment '{env_name}' already exists at {env_path}")
        
    else:
        
        try:
            
            print(f"|| Creating environment '{env_name}' at {env_path}...")
            print(f"|| Using Python command: {python_cmd}, '-m', 'venv', {env_path}")
            
            subprocess.check_call([python_cmd, '-m', 'venv', env_path])
            
            print(f"|| Environment '{env_name}' created at {env_path}")
            
        except subprocess.CalledProcessError as e:
            
            print(f"|| Failed to create environment: {e}")
            print("|| > Try running these commands manually:")
            
            if is_windows():
                
                bat_path = os.path.join(build_dir, 'create_env.bat')
                
                print(f"|| Run from {build_dir}:")
                print(f"|| {bat_path}")
                
            else:
                
                sh_path = os.path.join(build_dir, 'create_env.sh')
                
                print(f"|| Run from {build_dir}:")
                print(f"|| chmod +x {sh_path} && {sh_path}")
                
            return
        
    pip_path = os.path.join(env_path, 'Scripts' if is_windows() else 'bin', 'pip')
    
    print(f"|| Installing requirements from '{requirements_file}'...")
    print(f"|| Using pip command: {pip_path}, 'install', '-r', {requirements_file}")
    
    subprocess.check_call([pip_path, 'install', '-r', requirements_file])
    
    print(f"|| Requirements from '{requirements_file}' installed in '{env_name}'")



if __name__ == '__main__':
    create_env()
    
    check_python_version()
    notebook_setup()