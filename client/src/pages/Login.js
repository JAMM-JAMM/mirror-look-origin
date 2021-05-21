import styled from 'styled-components';
import Button from '@material-ui/core/Button';
import Box from '@material-ui/core/Box';
import NavBar from '../components/common/NavBar';
import WindowWrapper from '../components/common/WindowWrapper';

function Login() {
  function handleClick() {
    console.log('로그인 클릭했다!');
    window.location.href =
      'https://kauth.kakao.com/oauth/authorize?client_id=e7d2d5d4698806cd0bc1f0b197e41389&redirect_uri=http://localhost:3000/oauth/callback/kakao&response_type=code';
  }

  return (
    <WindowWrapper>
      <NavBar />
      <FlexDiv>
        <StyledLogo> Mirror-Look </StyledLogo>
        <KakaoButton onClick={handleClick} variant="contained">
          카카오로 로그인
        </KakaoButton>
      </FlexDiv>
    </WindowWrapper>
  );
}

const FlexDiv = styled('div')`
  display: flex;
  width: 100%;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`;

const KakaoButton = styled(Button)`
  background-color: #f7e600;
  color: #3a1d1d;
  padding: 5px 100px;
  font-weight: bold;
`;

const StyledLogo = styled(Box)`
  font-family: Rubik;
  font-style: normal;
  font-weight: bold;
  font-size: 50px;
  line-height: 40px;
  color: #8f00ff;
  margin: 50px;
`;

export default Login;
