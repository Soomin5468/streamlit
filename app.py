import streamlit as st
import simplenote
import pandas as pd

def get_simplenote_data(username, password):
    """
    Retrieve notes from Simplenote using the Simplenote API
    
    Args:
        username (str): Simplenote account email
        password (str): Simplenote account password
    
    Returns:
        list: List of notes with their details
    """
    # Initialize Simplenote client
    sn = simplenote.Simplenote(username, password)
    
    # Retrieve all notes
    notes = []
    try:
        # Get all notes
        all_notes, status = sn.get_note_list()
        
        # Fetch full details for each note
        for note_info in all_notes:
            note, _ = sn.get_note(note_info['key'])
            notes.append({
                'id': note_info['key'],
                'title': note.get('title', 'Untitled'),
                'content': note.get('content', ''),
                'created': note.get('created', ''),
                'modified': note.get('modified', ''),
                'tags': ', '.join(note.get('tags', []))
            })
        
        return notes
    
    except Exception as e:
        st.error(f"Error retrieving notes: {e}")
        return []

def main():
    st.title('Simplenote Notes Viewer')
    
    # Add input for Simplenote credentials
    with st.sidebar:
        username = st.text_input('Simplenote Email')
        password = st.text_input('Simplenote Password', type='password')
        
        # Fetch notes button
        if st.button('Fetch Notes'):
            if username and password:
                # Retrieve notes
                notes = get_simplenote_data(username, password)
                
                # Convert to DataFrame
                if notes:
                    df = pd.DataFrame(notes)
                    
                    # Display notes in a table
                    st.dataframe(df)
                    
                    # Additional filtering and analysis options
                    st.subheader('Note Analysis')
                    
                    # Tag distribution
                    st.write('Tag Distribution')
                    tag_counts = df['tags'].str.split(', ', expand=True).stack().value_counts()
                    st.bar_chart(tag_counts)
                    
                    # Notes per time period
                    df['created_date'] = pd.to_datetime(df['created'], unit='s')
                    st.write('Notes Created Over Time')
                    notes_per_month = df.groupby(pd.Grouper(key='created_date', freq='M')).size()
                    st.line_chart(notes_per_month)
                else:
                    st.warning('No notes found or error in retrieving notes')
            else:
                st.warning('Please enter Simplenote credentials')

if __name__ == '__main__':
    main()