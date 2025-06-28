#!/usr/bin/env python3
"""
Main runner for grief support sessions with customizable profiles.

This script reads configuration from session_config.py and runs grief support
experiments with detailed participant profiles using botex.

Usage:
    python run_configured_grief_sessions.py

Configuration:
    Edit session_config.py to customize the profiles and session settings.
"""

import logging
logging.basicConfig(level=logging.INFO)

import botex 
from grief_profiles import (
    get_random_profile, 
    get_predefined_profile, 
    create_custom_profile,
    get_all_predefined_profiles
)
from session_config import *
from datetime import datetime
import json

from dotenv import load_dotenv
load_dotenv('secrets.env')

def create_grief_persona_prompts(profile):
    """Create custom prompts for botex that incorporate the grief profile"""
    background = profile.get_background_prompt()
    response_guidance = profile.get_initial_response_guidance()
    
    custom_system_prompt = f"""You are participating in an online experiment about grief support interactions. 

{background}

Throughout this experiment:
- Stay in character as {profile.name}
- Draw on your specific experiences and emotional state  
- Respond authentically based on your personality and circumstances
- Consider your current needs and what kind of support would be most helpful

When making decisions about payment or responses, think about:
- Your current emotional state and needs
- Your financial situation and what feels reasonable to pay
- Whether the service provider seems trustworthy and understanding
- What kind of support would actually help you right now

Be genuine in your interactions, but remember this is an experiment designed to study support-seeking behavior."""

    custom_prompts = {
        "system": custom_system_prompt,
        "analyze_first_page_no_q": f"""Analyze this webpage as {profile.name}, someone who {profile.time_since_loss} lost their {profile.loss_type}. 

Read the content carefully and understand what this experiment is about. You are looking for {profile.support_preference} support and tend to be {profile.personality_trait} in your communication style.

What do you see on this page? What should you do next?""",

        "analyze_page_q": f"""As {profile.name}, analyze this page and the questions being asked. 

Remember your situation: You lost your {profile.loss_type} {profile.time_since_loss} under {profile.loss_circumstances} circumstances. You are seeking {profile.support_preference} support.

{response_guidance}

Answer the questions authentically based on your character and current emotional state."""
    }
    
    return custom_prompts

def save_session_log(session_info, profile, session_id):
    """Save session information to a log file"""
    if not EXPORT_DATA:
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"{EXPORT_PREFIX}_{timestamp}.json"
    
    log_data = {
        "timestamp": timestamp,
        "session_id": session_id,
        "profile": {
            "name": profile.name,
            "age": profile.age,
            "loss_type": profile.loss_type,
            "loss_circumstances": profile.loss_circumstances,
            "time_since_loss": profile.time_since_loss,
            "support_preference": profile.support_preference,
            "personality_trait": profile.personality_trait,
            "custom_details": profile.custom_details
        },
        "session_info": session_info
    }
    
    with open(log_filename, 'w') as f:
        json.dump(log_data, f, indent=2)
    
    print(f"Session log saved to: {log_filename}")

def run_single_configured_session(profile):
    """Run a single session with the given profile"""
    
    if SHOW_PROFILE_DETAILS:
        print(f"\nProfile Details:")
        print(f"  Name: {profile.name}, Age: {profile.age}")
        print(f"  Lost: {profile.loss_type} ({profile.loss_circumstances})")
        print(f"  Time since: {profile.time_since_loss}")
        print(f"  Seeking: {profile.support_preference} support")
        print(f"  Personality: {profile.personality_trait}")
        if profile.custom_details:
            print(f"  Details: {profile.custom_details}")
    
    # Create custom prompts
    custom_prompts = create_grief_persona_prompts(profile)
    
    # Initialize session
    print(f"\nInitializing grief support session...")
    grief_support = botex.init_otree_session(config_name="grief_support", npart=2)
    session_id = grief_support['session_id']
    print(f"Session ID: {session_id}")
    
    bot_urls = grief_support['bot_urls']
    
    try:
        print(f"Running {profile.name} as grief-stricken person...")
        # Run grief-stricken person with custom profile
        botex.run_single_bot(
            url=bot_urls[0],
            session_name="grief_support",
            session_id=session_id,
            participant_id=grief_support['participant_code'][0],
            user_prompts=custom_prompts,
            wait=False
        )
        
        print("Running service provider with default behavior...")
        # Run service provider with default behavior
        botex.run_single_bot(
            url=bot_urls[1],
            session_name="grief_support",
            session_id=session_id,
            participant_id=grief_support['participant_code'][1],
            wait=True
        )
        
        print(f"✓ Session completed successfully!")
        
        # Save session log
        save_session_log(grief_support, profile, session_id)
        
        return True
        
    except Exception as e:
        print(f"✗ Error in session: {e}")
        return False

def main():
    """Main function that runs sessions based on configuration"""
    
    print("=" * 60)
    print("GRIEF SUPPORT EXPERIMENT RUNNER")
    print("=" * 60)
    
    if DEMONSTRATE_PROMPTS_ONLY:
        print("Demonstrating custom prompts...")
        profile = get_predefined_profile(0)
        custom_prompts = create_grief_persona_prompts(profile)
        print(f"\nSample system prompt for {profile.name}:")
        print("-" * 40)
        print(custom_prompts["system"])
        return
    
    if RUN_COMPARATIVE_SESSIONS:
        print("Running comparative sessions with multiple profiles...")
        profiles = get_all_predefined_profiles()
        for i, profile in enumerate(profiles):
            print(f"\n--- Session {i+1}: {profile.name} ---")
            run_single_configured_session(profile)
        return
    
    if RUN_ALL_PROFILES:
        print("Running all predefined profiles...")
        profiles = get_all_predefined_profiles()
        for i, profile in enumerate(profiles):
            print(f"\n--- Profile {i+1}: {profile.name} ---")
            run_single_configured_session(profile)
        return
    
    # Single session configuration
    print(f"Configuration: {PROFILE_TYPE} profile, {NUM_SESSIONS} session(s)")
    
    for session_num in range(NUM_SESSIONS):
        print(f"\n=== Session {session_num + 1} of {NUM_SESSIONS} ===")
        
        # Get profile based on configuration
        if PROFILE_TYPE == "predefined":
            profile = get_predefined_profile(PREDEFINED_PROFILE_INDEX)
            print(f"Using predefined profile {PREDEFINED_PROFILE_INDEX}: {profile.name}")
            
        elif PROFILE_TYPE == "random":
            profile = get_random_profile()
            print(f"Using random profile: {profile.name}")
            
        elif PROFILE_TYPE == "custom":
            profile = create_custom_profile(**CUSTOM_PROFILE)
            print(f"Using custom profile: {profile.name}")
            
        else:
            raise ValueError(f"Unknown PROFILE_TYPE: {PROFILE_TYPE}")
        
        # Run the session
        success = run_single_configured_session(profile)
        
        if success:
            print(f"Session {session_num + 1} completed successfully!")
        else:
            print(f"Session {session_num + 1} failed!")
    
    print("\n" + "=" * 60)
    print("All sessions completed!")
    if EXPORT_DATA:
        print(f"Session logs saved with prefix: {EXPORT_PREFIX}")

if __name__ == "__main__":
    main()
