/**
 * 실제 채널에서 스크랩핑 해온 내용을 보여주는 아이템 컴포넌트입니다.
 * @property {Object} props
 * @property {Object} props.content
 * @property {string} props.content.title 제목 ( 채널의 내용 부분 )
 * @property {string} props.content.menus 메뉴 텍스트 ( OCR 추출 결과 )
 * @property {string} props.content.post_url 해당 게시글의 원문 URL
 */
const ContentItem = (props) => {
  const { content = {} } = props || {};
  const { title = "", menus = "", post_url } = content;
  // 컨텐츠 내용
  // OCR 조회 내용
  return (
    <div className="content-item-container">
      {/* 제목 ( 내용 ) */}
      <h2>{title}</h2>
      {/* OCR 텍스트 추출 결과 */}
      <div className="text-extraction">
        <a href={post_url}>원문 게시물로 이동하기</a>
        <p>{menus}</p>
      </div>
    </div>
  );
};

export default ContentItem;
